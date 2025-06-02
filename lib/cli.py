from lib.db.setup import Session
from lib.models.user import User
from lib.models.book import Book
from lib.models.lending import Lending

def start_cli():
    session = Session()
    print("\n📚 Welcome to the Book Lending CLI System!")

    while True:
        print("\nChoose an option:")
        print("1. Add user")
        print("2. Add book")
        print("3. List books")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Exit")

        choice = input(">> ")

        if choice == "1":
            name = input("User name: ")
            email = input("Email: ")
            session.add(User(name=name, email=email))
            session.commit()
            print("User added.")

        elif choice == "2":
            title = input("Book title: ")
            author = input("Author: ")
            session.add(Book(title=title, author=author, is_available=True))
            session.commit()
            print("Book added.")

        elif choice == "3":
            books = session.query(Book).all()
            for book in books:
                status = "Available" if book.is_available else "Borrowed"
                print(f"{book.id}. {book.title} by {book.author} — {status}")

        elif choice == "4":
            user_id = int(input("User ID: "))
            book_id = int(input("Book ID: "))
            book = session.query(Book).get(book_id)
            if book and book.is_available:
                lending = Lending(user_id=user_id, book_id=book_id)
                book.is_available = False
                session.add(lending)
                session.commit()
                print("Book borrowed.")
            else:
                print("Book not available.")

        elif choice == "5":
            book_id = int(input("Book ID to return: "))
            lending = session.query(Lending).filter_by(book_id=book_id, date_returned=None).first()
            if lending:
                lending.date_returned = datetime.now()
                lending.book.is_available = True
                session.commit()
                print("Book returned.")
            else:
                print("No active lending found for that book.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
from lib.db.setup import Session
from lib.models.user import User
from lib.models.book import Book
from lib.models.lending import Lending

def start_cli():
    session = Session()
    print("\n📚 Welcome to the Book Lending CLI System!")

    while True:
        print("\nChoose an option:")
        print("1. Add user")
        print("2. Add book")
        print("3. List books")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Exit")

        choice = input(">> ")

        if choice == "1":
            name = input("User name: ")
            email = input("Email: ")
            session.add(User(name=name, email=email))
            session.commit()
            print("User added.")

        elif choice == "2":
            title = input("Book title: ")
            author = input("Author: ")
            session.add(Book(title=title, author=author, is_available=True))
            session.commit()
            print("Book added.")

        elif choice == "3":
            books = session.query(Book).all()
            for book in books:
                status = "Available" if book.is_available else "Borrowed"
                print(f"{book.id}. {book.title} by {book.author} — {status}")

        elif choice == "4":
            user_id = int(input("User ID: "))
            book_id = int(input("Book ID: "))
            book = session.query(Book).get(book_id)
            if book and book.is_available:
                lending = Lending(user_id=user_id, book_id=book_id)
                book.is_available = False
                session.add(lending)
                session.commit()
                print("Book borrowed.")
            else:
                print("Book not available.")

        elif choice == "5":
            book_id = int(input("Book ID to return: "))
            lending = session.query(Lending).filter_by(book_id=book_id, date_returned=None).first()
            if lending:
                lending.date_returned = datetime.now()
                lending.book.is_available = True
                session.commit()
                print("Book returned.")
            else:
                print("No active lending found for that book.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
