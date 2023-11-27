from lib.book_repository import *
from lib.book import *


def test_list_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)

    books = repo.all()

    assert len(books) >= 2

    assert books[0].id == 1
    assert books[0].title == "Nineteen Eighty-Four"
    assert books[0].author_name == "George Orwell"

    assert books[1].id == 2
    assert books[1].title == "Mrs Dalloway"
    assert books[1].author_name == "Virginia Woolf"
