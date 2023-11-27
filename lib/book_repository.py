from lib.book import *


class BookRepository:
    # init connection
    def __init__(self, connection):
        self._connection = connection

    # Selecting all records
    # No arguments
    def all(self):
        # Executes the SQL query:
        # SELECT id, name, author_name FROM book_store;

        # Returns an array of Book objects.
        rows = self._connection.execute("SELECT * from books1")
        books = []
        for row in rows:
            item = Books(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books
