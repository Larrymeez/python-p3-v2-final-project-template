from datetime import datetime
from lib.models.user import User
from lib.models.book import Book
from lib.models.lending import Lending
from lib.db.setup import Session

session = Session()

def start_cli():
    while True:
        print("\n=== Book Lending CLI ===")
        print("1. Add User")
        print("2. Add Book")
        print("3. View All Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            user = User(name=name, email=email)
            session.add(user)
            session.commit()
            print(f"User '{name}' added.")

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title=title, author=author, is_available=True)
            session.add(book)
            session.commit()
            print(f"Book '{title}' by {author} added.")

        elif choice == "3":
            books = session.query(Book).all()
            print("\nAll Books:")
            for book in books:
                status = "Available" if book.is_available else "Borrowed"
                print(f"{book.id}: {book.title} by {book.author} - {status}")

        elif choice == "4":  # Borrow Book
            users = session.query(User).all()
            print("\nRegistered Users:")
            for user in users:
                print(f"{user.id}: {user.name} ({user.email})")

            try:
                user_id = int(input("Enter User ID: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            user = session.query(User).get(user_id)
            if not user:
                print("User not found.")
                continue

            books = session.query(Book).filter_by(is_available=True).all()
            if not books:
                print("No books are currently available.")
                continue

            print("\nAvailable Books:")
            for book in books:
                print(f"{book.id}: {book.title} by {book.author}")

            try:
                book_id = int(input("Enter Book ID to borrow: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            book = session.query(Book).get(book_id)
            if not book or not book.is_available:
                print("Book not available.")
                continue

            lending = Lending(user_id=user.id, book_id=book.id, borrowed_date=datetime.now())
            book.is_available = False

            session.add(lending)
            session.commit()
            print(f"{user.name} borrowed '{book.title}'.")

        elif choice == "5":  # Return Book
            users = session.query(User).all()
            print("\nRegistered Users:")
            for user in users:
                print(f"{user.id}: {user.name} ({user.email})")

            try:
                user_id = int(input("Enter User ID: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            user = session.query(User).get(user_id)
            if not user:
                print("User not found.")
                continue

            active_loans = (
                session.query(Lending)
                .filter_by(user_id=user.id, returned_date=None)
                .join(Book)
                .all()
            )

            if not active_loans:
                print("No books to return for this user.")
                continue

            print("\nBooks currently borrowed by user:")
            for lending in active_loans:
                book = lending.book
                print(f"{book.id}: {book.title} by {book.author}")

            try:
                book_id = int(input("Enter Book ID to return: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            lending_to_return = next((l for l in active_loans if l.book_id == book_id), None)
            if not lending_to_return:
                print("Invalid Book ID or not borrowed by this user.")
                continue

            lending_to_return.returned_date = datetime.now()
            lending_to_return.book.is_available = True
            session.commit()
            print(f"'{lending_to_return.book.title}' has been returned.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

