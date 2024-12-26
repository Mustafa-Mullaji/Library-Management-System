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
       self.books.append(book)
    

