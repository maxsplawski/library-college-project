import unittest
from unittest.mock import Mock, patch, MagicMock

from cli import CLI
from entities import User


class TestServices(unittest.TestCase):
    def setUp(self):
        self.mock_auth_service = Mock()
        self.mock_book_service = Mock()
        self.cli = CLI(self.mock_auth_service, self.mock_book_service)

    @patch("builtins.input", side_effect=["user@example.com"])
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_can_login(self, mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        self.mock_auth_service.login.return_value = True

        result = self.cli.show_login()

        self.assertTrue(result)
        self.mock_auth_service.login.assert_called_once_with("user@example.com")
        mock_print.assert_any_call("Logged in")

    @patch("builtins.input", side_effect=["user@example.com", "password"])
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_is_shown_error_message_on_login_failure(self,  mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        self.mock_auth_service.login.return_value = False

        result = self.cli.show_login()

        self.assertFalse(result)
        self.mock_auth_service.login.assert_called_once_with("user@example.com")
        mock_print.assert_any_call("Invalid credentials, please try again")

    @patch("builtins.input", side_effect=["user@example.com", "password"])
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_can_sign_up(self,  mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        self.mock_auth_service.get_user.return_value = None
        self.mock_auth_service.register.return_value = None

        self.cli.show_sign_up()

        self.mock_auth_service.get_user.assert_called_with("user@example.com")
        self.mock_auth_service.register.assert_called_with("user@example.com", "password")
        mock_print.assert_any_call("Registered")

    @patch("builtins.input", side_effect=["user@example.com", "user@company.com"])
    @patch("getpass.getpass", side_effect=["password", "password", "password", "password"])
    @patch("builtins.print")
    def test_user_is_shown_error_message_on_email_taken(self, mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        self.mock_auth_service.get_user.side_effect = lambda email: MagicMock() if email == "user@example.com" else None
        self.mock_auth_service.register.return_value = None

        self.cli.show_sign_up()

        self.mock_auth_service.get_user.assert_called_with("user@company.com")
        mock_print.assert_any_call("Email is taken")