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
    
    


    

