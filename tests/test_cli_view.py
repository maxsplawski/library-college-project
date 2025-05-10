import unittest
from unittest.mock import Mock, patch, MagicMock

from domain.entities import Book
from infrastructure.view import CommandLineInterfaceView
from settings import EXPORT_DESTINATION


class TestCommandLineInterfaceView(unittest.TestCase):
    def setUp(self):
        self.mock_auth_service = Mock()
        self.mock_book_service = Mock()
        self.cli_view = CommandLineInterfaceView(self.mock_auth_service, self.mock_book_service)

    @patch("builtins.input", return_value="user@example.com")
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_can_login(self, mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        self.mock_auth_service.login.return_value = True

        result = self.cli_view.attempt_login()

        self.assertTrue(result)
        self.mock_auth_service.login.assert_called_once_with("user@example.com", "password")
        mock_print.assert_any_call("Logged in")

    @patch("builtins.input", return_value="user@example.com")
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_is_shown_error_message_on_login_failure(self, mock_print: MagicMock, mock_getpass: MagicMock,
                                                          mock_input: MagicMock):
        self.mock_auth_service.login.return_value = False

        result = self.cli_view.attempt_login()

        self.assertFalse(result)
        self.mock_auth_service.login.assert_called_once_with("user@example.com", "password")
        mock_print.assert_any_call("Invalid credentials, please try again")

    @patch("builtins.input", return_value="user@example.com")
    @patch("getpass.getpass", return_value="password")
    @patch("builtins.print")
    def test_user_can_sign_up(self, mock_print: MagicMock, mock_getpass: MagicMock, mock_input: MagicMock):
        self.mock_auth_service.get_user.return_value = None
        self.mock_auth_service.register.return_value = None

        self.cli_view.attempt_registration()

        self.mock_auth_service.get_user.assert_called_with("user@example.com")
        self.mock_auth_service.register.assert_called_with("user@example.com", "password")
        mock_print.assert_any_call("Registered")

    @patch("builtins.input", side_effect=["user@example.com", "user@company.com"])
    @patch("getpass.getpass", side_effect=["password", "password", "password", "password"])
    @patch("builtins.print")
    def test_user_is_shown_error_message_on_email_taken(self, mock_print: MagicMock, mock_getpass: MagicMock,
                                                        mock_input: MagicMock):
        self.mock_auth_service.get_user.side_effect = lambda email: MagicMock() if email == "user@example.com" else None
        self.mock_auth_service.register.return_value = None

        self.cli_view.attempt_registration()

        self.mock_auth_service.get_user.assert_called_with("user@company.com")
        mock_print.assert_any_call("Email is taken")

    @patch("builtins.input", side_effect=["user@example.com", "user@example.com"])
    @patch("getpass.getpass", side_effect=["password", "pazzword", "password", "password"])
    @patch("builtins.print")
    def test_user_is_shown_error_message_on_password_mismatch(self, mock_print: MagicMock, mock_getpass: MagicMock,
                                                              mock_input: MagicMock):
        self.mock_auth_service.get_user.return_value = None
        self.mock_auth_service.register.return_value = None

        self.cli_view.attempt_registration()

        self.mock_auth_service.get_user.assert_called_with("user@example.com")
        mock_print.assert_any_call("Passwords do not match")

    @patch("builtins.print")
    def test_user_can_get_books(self, mock_print: MagicMock):
        books = [
            Book(1, "1234", "Author 1", "Title 1", 10),
            Book(2, "2345", "Author 2", "Title 2", 20)
        ]
        self.mock_book_service.get_books.return_value = books

        self.cli_view.route_command("1")

        self.mock_book_service.get_books.assert_called_once()
        mock_print.assert_any_call("All books currently in the library:")
        for book in books:
            mock_print.assert_any_call(book)

    @patch("builtins.input", return_value="1234")
    @patch("builtins.print")
    def test_user_can_get_book(self, mock_print: MagicMock, mock_input: MagicMock):
        book = Book(1, "1234", "Author 1", "Title 1", 10)
        self.mock_book_service.get_book.return_value = book

        self.cli_view.route_command("2")

        self.mock_book_service.get_book.assert_called_with("1234")
        mock_print.assert_any_call(book)

    @patch("builtins.input", return_value="1234")
    @patch("builtins.print")
    def test_user_is_shown_error_message_when_book_not_found_on_get_book_attempt(self, mock_print: MagicMock,
                                                                                 mock_input: MagicMock):
        self.mock_book_service.get_book.return_value = None

        self.cli_view.route_command("2")

        self.mock_book_service.get_book.assert_called_with("1234")
        mock_print.assert_any_call("No book found")

    @patch("builtins.input", side_effect=["1234", "Author 1", "Title 1", 10])
    @patch("builtins.print")
    def test_user_can_add_book(self, mock_print: MagicMock, mock_input: MagicMock):
        book = Book(1, "1234", "Author 1", "Title 1", 10)
        self.mock_book_service.add_book.return_value = book

        self.cli_view.route_command("3")

        # self.mock_book_service.add_book.assert_called_with(Book(ANY, "1234", "Author 1", "Title 1", 10))
        mock_print.assert_any_call(f"Added {book}")

    @patch("builtins.input", side_effect=["1234", "Updated Author", "Updated Title", 20])
    @patch("builtins.print")
    def test_user_can_update_book(self, mock_print: MagicMock, mock_input: MagicMock):
        book = Book(1, "1234", "Author 1", "Title 1", 10)
        updated_book = Book(1, "1234", "Updated Author", "Updated Title", 20)
        self.mock_book_service.get_book.return_value = book
        self.mock_book_service.update_book.return_value = updated_book

        self.cli_view.route_command("4")

        self.mock_book_service.get_book.assert_called_with("1234")
        self.mock_book_service.update_book.assert_called_with(book)
        mock_print.assert_any_call(f"Updated {updated_book}")

    @patch("builtins.input", return_value="1234")
    @patch("builtins.print")
    def test_user_is_shown_error_message_when_book_not_found_on_book_update_attempt(self, mock_print: MagicMock,
                                                                                    mock_input: MagicMock):
        self.mock_book_service.get_book.return_value = None

        self.cli_view.route_command("4")

        self.mock_book_service.get_book.assert_called_with("1234")
        self.mock_book_service.update_book.assert_not_called()
        mock_print.assert_any_call("No book found")

    @patch("builtins.input", return_value="1234")
    @patch("builtins.print")
    def test_user_can_delete_book(self, mock_print: MagicMock, mock_input: MagicMock):
        self.cli_view.route_command("5")

        self.mock_book_service.delete_book.assert_called_with("1234")
        mock_print.assert_any_call("Deleted a book with ISBN: 1234")

    @patch("builtins.input", return_value="1234")
    @patch("builtins.print")
    def test_user_is_shown_error_message_when_book_not_found_on_book_delete_attempt(self, mock_print: MagicMock,
                                                                                    mock_input: MagicMock):
        self.mock_book_service.get_book.return_value = None

        self.cli_view.route_command("5")

        self.mock_book_service.get_book.assert_called_with("1234")
        self.mock_book_service.delete_book.assert_not_called()
        mock_print.assert_any_call("No book found")

    @patch("builtins.print")
    def test_user_can_export_books(self, mock_print: MagicMock):
        self.mock_book_service.export_books.return_value = None

        self.cli_view.route_command("6")

        self.mock_book_service.export_books.assert_called_with(EXPORT_DESTINATION)

    @patch("builtins.print")
    @patch("sys.exit")
    def test_user_can_exit(self, mock_exit: MagicMock, mock_print: MagicMock):
        self.cli_view.route_command("7")

        mock_print.assert_any_call("Goodbye!")
        mock_exit.assert_called_once_with(0)

    @patch("builtins.print")
    def test_user_is_shown_error_message_on_invalid_choice(self, mock_print: MagicMock):
        self.cli_view.route_command("invalid")

        mock_print.assert_any_call("Invalid choice")


if __name__ == "__main__":
    unittest.main()
