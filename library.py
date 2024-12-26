class Book:
    def __init__(self, isbn, title, author, publication_year):
        if not isbn.isdigit() or len(isbn) != 5:
            raise ValueError("ISBN must be a 5-digit number.")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    raise ValueError(f"Book with ISBN {isbn} is already borrowed.")
                book.is_borrowed = True
                return True
        raise ValueError(f"Book with ISBN {isbn} not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    raise ValueError(f"Book with ISBN {isbn} was not borrowed.")
                book.is_borrowed = False
                return True
        raise ValueError(f"Book with ISBN {isbn} not found.")

    def view_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        return available_books


def display_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. View Available Books")
    print("5. Exit")


def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            # Add Book
            isbn = input("Enter ISBN (5 digits): ")
            title = input("Enter book title: ")
            author = input("Enter author: ")
            publication_year = input("Enter publication year: ")

            try:
                book = Book(isbn, title, author, publication_year)
                library.add_book(book)
                print(f"Book '{title}' added successfully.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            # Borrow Book
            isbn = input("Enter ISBN of the book to borrow: ")
            try:
                library.borrow_book(isbn)
                print(f"Book with ISBN {isbn} borrowed successfully.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            # Return Book
            isbn = input("Enter ISBN of the book to return: ")
            try:
                library.return_book(isbn)
                print(f"Book with ISBN {isbn} returned successfully.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            # View Available Books
            available_books = library.view_available_books()
            if available_books:
                print("\nAvailable Books:")
                for book in available_books:
                    print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
            else:
                print("No books available.")

        elif choice == "5":
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

    

