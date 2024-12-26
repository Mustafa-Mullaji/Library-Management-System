import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("12345", "The Time Keeper", "Mitch Albom", 2012)
        library.add_book(book)
        self.assertEqual(len(library.books), 1)

    def test_valid_isbn(self):
        # Valid ISBN
        book = Book("24567", "Valid Book", "Author", 2000)
        self.assertEqual(book.isbn, "24567")

    def test_invalid_isbn_non_digit(self):
        # ISBN with non-digit characters
        with self.assertRaises(ValueError) as context:
            Book("1234X", "Invalid Book", "Author", 2000)
        self.assertEqual(str(context.exception), "ISBN must be a 5-digit number.")

    def test_invalid_isbn_wrong_length(self):
        # ISBN not 5 digits long
        with self.assertRaises(ValueError) as context:
            Book("123", "Short ISBN Book", "Author", 2000)
        self.assertEqual(str(context.exception), "ISBN must be a 5-digit number.")
    
    def test_add_book_unique_isbn(self):
         library = Library()
         book1 = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
         book2 = Book("12345", "1984", "George Orwell", 1949)
         library.add_book(book1)
         with self.assertRaises(ValueError):  
          library.add_book(book2)
    
    def test_borrow_book(self):
       library = Library()
       book = Book("54321", "To Kill a Mockingbird", "Harper Lee", 1960)
       library.add_book(book)
       result = library.borrow_book("54321")   
       self.assertTrue(result)
       self.assertTrue(book.is_borrowed)

    def test_borrow_unavailable_book(self):
       library = Library()
       book = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
       library.add_book(book)
       library.borrow_book("12345")
       with self.assertRaises(ValueError): 
        library.borrow_book("12345")
    
    def test_return_book_not_borrowed(self):
      library = Library()
      book = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
      library.add_book(book)
      with self.assertRaises(ValueError): 
        library.return_book("12345")

    def test_view_available_books(self):
        library = Library()
        book1 = Book("12345", "Valid Book", "Author", 2000)
        book2 = Book("67890", "Another Book", "Author", 2001)
        library.add_book(book1)
        library.add_book(book2)
        library.borrow_book("12345")
        available_books = library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].isbn, "67890")



if __name__ == "__main__":
    unittest.main()
