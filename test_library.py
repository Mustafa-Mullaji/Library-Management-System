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


if __name__ == "__main__":
    unittest.main()
