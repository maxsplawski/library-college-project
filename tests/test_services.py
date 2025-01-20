import unittest
from unittest.mock import Mock, patch, MagicMock

from cli import CLI


class TestServices(unittest.TestCase):
    def setUp(self):
        self.mock_auth_service = Mock()
        self.mock_book_service = Mock()
        self.cli = CLI(self.mock_auth_service, self.mock_book_service)

    @patch("builtins.input", side_effect=["user@example.com", "password"])
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_can_login(self, mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        # given
        self.mock_auth_service.login.return_value = True

        # when
        result = self.cli.show_login()

        # then
        self.assertTrue(result)
        self.mock_auth_service.login.assert_called_once_with("user@example.com", "password")
        mock_print.assert_any_call("Logged in")

    @patch("builtins.input", side_effect=["user@example.com", "password"])
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_is_shown_error_message_on_login_failure(self,  mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        # given
        self.mock_auth_service.login.return_value = False

        # when
        result = self.cli.show_login()

        # then
        self.assertFalse(result)
        self.mock_auth_service.login.assert_called_once_with("user@example.com", "password")
        mock_print.assert_any_call("Invalid credentials, please try again")

    @patch("builtins.input", side_effect=["user@example.com", "password", "password"])
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_can_sign_up(self,  mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        # given
        self.mock_auth_service.get_user.return_value = None