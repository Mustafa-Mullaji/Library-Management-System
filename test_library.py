import unittest
from library import Library, Book 
import os
import subprocess

# Test class for the Library Management System
class TestLibrary(unittest.TestCase):

    # Test for adding a book to the library
    def test_add_book(self):
        library = Library() 
        book = Book("12345", "The Time Keeper", "Mitch Albom", 2012)  
        library.add_book(book)  
        self.assertEqual(len(library.books), 1)

    # Test for checking a valid ISBN
    def test_valid_isbn(self):
        book = Book("24567", "Valid Book", "Author", 2000)  
        self.assertEqual(book.isbn, "24567")  

    # Test for invalid ISBN (non-digit characters)
    def test_invalid_isbn_non_digit(self):
        with self.assertRaises(ValueError) as context:  
            Book("1234X", "Invalid Book", "Author", 2000)  
        self.assertEqual(str(context.exception), "ISBN must be a 5-digit number.")  

    # Test for invalid ISBN (wrong length)
    def test_invalid_isbn_wrong_length(self):
        with self.assertRaises(ValueError) as context:  
            Book("123", "Short ISBN Book", "Author", 2000)  
        self.assertEqual(str(context.exception), "ISBN must be a 5-digit number.")  

    # Test for adding a book with a duplicate ISBN
    def test_add_book_unique_isbn(self):
        library = Library()  
        book1 = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)  
        book2 = Book("12345", "1984", "George Orwell", 1949)  
        library.add_book(book1)  
        with self.assertRaises(ValueError): 
            library.add_book(book2)

    # Test for borrowing a book successfully
    def test_borrow_book(self):
        library = Library()  
        book = Book("54321", "To Kill a Mockingbird", "Harper Lee", 1960)  
        library.add_book(book) 
        result = library.borrow_book("54321") 
        self.assertTrue(result)  
        self.assertTrue(book.is_borrowed)  

    # Test for trying to borrow a book that is already borrowed
    def test_borrow_unavailable_book(self):
        library = Library()  
        book = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)  
        library.add_book(book)  
        library.borrow_book("12345")  
        with self.assertRaises(ValueError):  
            library.borrow_book("12345")

    # Test for returning a book that was not borrowed
    def test_return_book_not_borrowed(self):
        library = Library()  
        book = Book("12345", "The Great Gatsby", "F. Scott Fitzgerald", 1925)  
        library.add_book(book)  
        with self.assertRaises(ValueError):  
            library.return_book("12345")

    # Test for viewing available books in the library
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

def run_tests():
    """Runs tests and generates an HTML report."""
    print("Running tests...")
    try:
        # Ensure pytest is used to run the tests
        subprocess.run(["pytest", "test_library.py", "--html=report.html", "--self-contained-html"], check=True)
        print("Test report generated: report.html")
    except subprocess.CalledProcessError as e:
        print(f"Error during test execution: {e}")


# Run the test cases
if __name__ == "__main__":
    unittest.main()
    run_tests() 
