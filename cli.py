from config import APP_NAME


class CLI:
    def __init__(self, controller):
        self.controller = controller

    def show_menu(self):
        print(f"\n--- {APP_NAME} ---")
        print("1. Show all books")
        print("2. Show a book")
        print("3. Add a book")
        print("4. Update a book")
        print("5. Delete a book")
        choice = int(input("Enter your choice (1-5): "))
        return choice

    def route_command(self, choice: int):
        match choice:
            case 1:
                self.controller.get_books()
            case 2:
                self.controller.get_book()
            case 3:
                self.controller.add_book()
            case 4:
                self.controller.update_book()
            case 5:
                self.controller.delete_book()

