import getpass
import sys

from config import APP_NAME
from services import AuthService, BookService
from entities import Book


class CLI:
    def __init__(self, auth_service: AuthService, book_service: BookService):
        self.auth_service = auth_service
        self.book_service = book_service

    def show_auth_menu(self):
        print(f"Welcome back to {APP_NAME}!")
        print("Please log in to continue")
        while True:
            email = input("Email: ")
            password = getpass.getpass("Password: ")
            success = self.auth_service.login(email, password)
            if success:
                print("Logged in")
                return
            else:
                print("Invalid credentials, please try again")

    def show_main_menu(self) -> str:
        while True:
            print(f"\n--- {APP_NAME} ---")
            print("1. Show all books")
            print("2. Show a book")
            print("3. Add a book")
            print("4. Update a book")
            print("5. Delete a book")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")
            return choice

    def route_command(self, choice: int):
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
            book_to_update.author = input("Author: ")
            book_to_update.title = input("Title: ")
            book_to_update.pages = int(input("Pages: "))
            book = self.book_service.update_book(book_to_update)
            print(f"Updated {book}")
        elif choice == "5":
            isbn = input("Provide the book's ISBN: ")
            self.book_service.delete_book(isbn)
            print(f"Deleted a book with ISBN: {isbn}")
        elif choice == "6":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice")

