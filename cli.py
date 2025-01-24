import getpass
import sys

from entities import Book
from services import AuthService, BookService
from settings import APP_NAME


class CLI:
    def __init__(self, auth_service: AuthService, book_service: BookService):
        self.auth_service = auth_service
        self.book_service = book_service

    def show_auth_menu(self):
        print(f"Welcome back to {APP_NAME}!")
        while True:
            print("1. Login")
            print("2. Sign up")
            auth_method = input("Enter your choice (1-2): ")
            if auth_method == "1":
                login_success = self.show_login()
                if login_success:
                    return
            elif auth_method == "2":
                self.show_sign_up()
                return
            else:
                print("Invalid choice")

    def show_login(self) -> bool:
        while True:
            email = input("Email: ")
            password = getpass.getpass("Password: ")
            success = self.auth_service.login(email, password)
            if success:
                print("Logged in")
                return True
            else:
                print("Invalid credentials, please try again")
                return False

    def show_sign_up(self):
        while True:
            email = input("Email: ") # validate
            user = self.auth_service.get_user(email)
            password = getpass.getpass("Password: ")
            password_confirmation = getpass.getpass("Confirm password: ")
            if password == password_confirmation and user is None:
                self.auth_service.register(email, password)
                print("Registered")
                return
            elif user:
                print("Email is taken")
            else:
                print("Passwords do not match")

    def show_main_menu(self) -> str:
        print("1. Show all books")
        print("2. Show a book")
        print("3. Add a book")
        print("4. Update a book")
        print("5. Delete a book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        return choice

    def route_command(self, choice: str):
        if choice == "1":
            books = self.book_service.get_books()
            print("All books currently in the library:")
            for book in books:
                print(book)
        elif choice == "2":
            isbn = input("Provide the book's ISBN: ")
            book = self.book_service.get_book(isbn)
            if book:
                print(book)
            else:
                print("No book found")
        elif choice == "3":
            isbn = input("ISBN: ")
            author = input("Author: ")
            title = input("Title: ")
            pages = int(input("Pages: "))
            book = self.book_service.add_book(Book(None, isbn, author, title, pages))
            print(f"Added {book}")
        elif choice == "4":
            isbn = input("Provide the book's ISBN: ")
            book_to_update = self.book_service.get_book(isbn)
            if book_to_update is None:
                print("No book found")
                return
            book_to_update.author = input("Author: ")
            book_to_update.title = input("Title: ")
            book_to_update.pages = int(input("Pages: "))
            book = self.book_service.update_book(book_to_update)
            print(f"Updated {book}")
        elif choice == "5":
            isbn = input("Provide the book's ISBN: ")
            book_to_delete = self.book_service.get_book(isbn)
            if book_to_delete is None:
                print("No book found")
                return
            self.book_service.delete_book(isbn)
            print(f"Deleted a book with ISBN: {isbn}")
        elif choice == "6":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice")
