import getpass
import sys

from domain.domains import AuthDomain, BookDomain
from domain.entities import Book
from domain.view import View


class CommandLineInterfaceView(View):
    def __init__(self, auth_domain: AuthDomain, book_domain: BookDomain):
        self.auth_domain = auth_domain
        self.book_domain = book_domain

    def authenticate(self) -> bool:
        print("1. Login")
        print("2. Sign up")
        auth_method = input("Enter your choice (1-2): ")
        if auth_method == "1":
            return self.attempt_login()
        elif auth_method == "2":
            return self.attempt_registration()
        else:
            print("Invalid choice")
            return False

    def attempt_login(self) -> bool:
        while True:
            email = input("Email: ")
            password = getpass.getpass("Password: ")
            success = self.auth_domain.login(email, password)
            if success:
                print("Logged in")
                return True
            else:
                print("Invalid credentials, please try again")
                return False

    def attempt_registration(self) -> bool:
        while True:
            email = input("Email: ")  # validate
            user = self.auth_domain.get_user(email)
            password = getpass.getpass("Password: ")
            password_confirmation = getpass.getpass("Confirm password: ")
            if password == password_confirmation and user is None:
                self.auth_domain.register(email, password)
                print("Registered")
                return True
            elif user:
                print("Email is taken")
            else:
                print("Passwords do not match")

    def get_command(self) -> str:
        print("1. Show all books")
        print("2. Show a book")
        print("3. Add a book")
        print("4. Update a book")
        print("5. Delete a book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        return choice

    def route_command(self, command: str) -> None:
        if command == "1":
            books = self.book_domain.get_books()
            print("All books currently in the library:")
            for book in books:
                print(book)
        elif command == "2":
            isbn = input("Provide the book's ISBN: ")
            book = self.book_domain.get_book(isbn)
            if book:
                print(book)
            else:
                print("No book found")
        elif command == "3":
            isbn = input("ISBN: ")
            author = input("Author: ")
            title = input("Title: ")
            pages = int(input("Pages: "))
            book = self.book_domain.add_book(Book(None, isbn, author, title, pages))
            print(f"Added {book}")
        elif command == "4":
            isbn = input("Provide the book's ISBN: ")
            book_to_update = self.book_domain.get_book(isbn)
            if book_to_update is None:
                print("No book found")
                return
            book_to_update.author = input("Author: ")
            book_to_update.title = input("Title: ")
            book_to_update.pages = int(input("Pages: "))
            book = self.book_domain.update_book(book_to_update)
            print(f"Updated {book}")
        elif command == "5":
            isbn = input("Provide the book's ISBN: ")
            book_to_delete = self.book_domain.get_book(isbn)
            if book_to_delete is None:
                print("No book found")
                return
            self.book_domain.delete_book(isbn)
            print(f"Deleted a book with ISBN: {isbn}")
        elif command == "6":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice")
