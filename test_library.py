import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("12345", "The Time Keeper", "Mitch Albom", 2012)
        library.add_book(book)  # Method not implemented yet
        self.assertEqual(len(library.books), 1)

if __name__ == "__main__":
    unittest.main()
