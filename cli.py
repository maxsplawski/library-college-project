import sys

from config import APP_NAME
from controllers import AuthController, BookController
from entities import Book


class CLI:
    def __init__(self, auth_controller: AuthController, book_controller: BookController):
        self.auth_controller = auth_controller
        self.book_controller = book_controller

    def show_auth_menu(self):
        print(f"Welcome back to {APP_NAME}!")
        print("1. Log in")


    def show_main_menu(self):
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
        match choice:
            case "1":
                books = self.book_controller.get_books()
                print("All books currently in the library:")
                for book in books:
                    print(book)
            case "2":
                isbn = input("Provide the book's ISBN: ")
                book = self.book_controller.get_book(isbn)
                if book:
                    print(book)
                else:
                    print("No book found")
            case "3":
                isbn = input("ISBN: ")
                author = input("Author: ")
                title = input("Title: ")
                pages = int(input("Pages: "))
                book = self.book_controller.add_book(Book(None, isbn, author, title, pages))
                print(f"Added {book}")
            case "4":
                isbn = input("Provide the book's ISBN: ")
                book_to_update = self.book_controller.get_book(isbn)
                if book_to_update is None:
                    print("No book found")
                book_to_update.author = input("Author: ")
                book_to_update.title = input("Title: ")
                book_to_update.pages = int(input("Pages: "))
                book = self.book_controller.update_book(book_to_update)
                print(f"Updated {book}")
            case "5":
                isbn = input("Provide the book's ISBN: ")
                self.book_controller.delete_book(isbn)
                print(f"Deleted a book with ISBN: {isbn}")
            case "6":
                print("Goodbye!")
                sys.exit(0)
            case _:
                print("Invalid choice")

