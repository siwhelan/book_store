from lib.book import *

# book object construction works as intended
# with id, title and author_name


def test_book_construction():
    book = Books(5, "Book Title", "Well Known Author")
    assert book.id == 5
    assert book.title == "Book Title"
    assert book.author_name == "Well Known Author"


# test_books_format_correctly
def test_books_format_correctly():
    book = Books(5, "Book Title", "Well Known Author")
    assert str(book) == "Book(5, Book Title, Well Known Author)"
