import json
import os

class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books and their count
        self.users = {}  # Dictionary to store user data
        self.load_data()  # Load previous data from file

    def add_book(self, title, category, copies=1):
        if title in self.books:
            self.books[title]['copies'] += copies
        else:
            self.books[title] = {'category': category, 'copies': copies}
        print(f'📖 Added "{title}" under "{category}" with {copies} copies.')
        self.save_data()

    def display_books(self):
        if not self.books:
            print("📚 No books available.")
        else:
            print("\n📖 Available Books:")
            for title, info in self.books.items():
                print(f' - {title} ({info["category"]}) - {info["copies"]} copies')

    def borrow_book(self, user, title):
        if title in self.books and self.books[title]['copies'] > 0:
            self.books[title]['copies'] -= 1
            self.users.setdefault(user, []).append(title)
            print(f'✅ {user} borrowed "{title}".')
        else:
            print(f'❌ Sorry, "{title}" is not available.')
        self.save_data()

    def return_book(self, user, title):
        if user in self.users and title in self.users[user]:
            self.users[user].remove(title)
            self.books[title]['copies'] += 1
            print(f'🔄 {user} returned "{title}".')
        else:
            print(f'❌ {user} did not borrow "{title}".')
        self.save_data()

    def save_data(self):
        """Save books and users to a file for persistence."""
        with open("library_data.json", "w") as file:
            json.dump({"books": self.books, "users": self.users}, file)

    def load_data(self):
        """Load books and users from the file if it exists."""
        if os.path.exists("library_data.json"):
            with open("library_data.json", "r") as file:
                data = json.load(file)
                self.books = data.get("books", {})
                self.users = data.get("users", {})
                
def main():
    library = Library()

    while True:
        print("\n📚 Library Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            category = input("Enter book category (Fiction, Science, etc.): ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, category, copies)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            user = input("Enter your name: ")
            book = input("Enter book name to borrow: ")
            library.borrow_book(user, book)

        elif choice == "4":
            user = input("Enter your name: ")
            book = input("Enter book name to return: ")
            library.return_book(user, book)

        elif choice == "5":
            print("📚 Exiting the Library System. Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

