import sys

from config import APP_NAME


class CLI:
    def __init__(self, auth_controller, book_controller):
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
        choice = int(input("Enter your choice (1-5): "))
        return choice

    def route_command(self, choice: int):
        match choice:
            case 1:
                self.book_controller.get_books()
            case 2:
                self.book_controller.get_book()
            case 3:
                self.book_controller.add_book()
            case 4:
                self.book_controller.update_book()
            case 5:
                self.book_controller.delete_book()
            case 6:
                print("Goodbye!")
                sys.exit(0)
            case _:
                print("Invalid choice")

