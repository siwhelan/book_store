

## 1. Design and create the Table

See seeds/book_store.sql


```
# EXAMPLE

Table: book_store

Columns:
id | title | author_name
```

## 2. Define the class names


```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book_store.py)
class Books


# Repository class
# (in lib/book_repository.py)
class BookRepository

```

## 3. Implement the Model class


```python
# Table name: book_store

# Model book
# (in lib/.py)

class Books:
    def __init__(self):
        self.id = id
        self.title = title
        self.author_name = author_name

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        pass

    # This method makes it look nicer when we print a book
    def __repr__(self):
        pass


```

## 4. Define the Repository Class interface


```python
# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class BookRepository():

    # init connection 
    def __init__(self, connection):
        self._connection = connection
    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, author_name FROM book_store;

        # Returns an array of Book objects.

```

## 5. Write Test Examples

```python
# EXAMPLES

# book object construction works as intended
# with id, title and author_name

book = Books(5, 'Book Title', 'Well Known Author')
book.id # => 5
book.title # => 'Book Title'
book.author # => 'Well Known Author'

# Get all books

repo = BookRepository()

books = repo.all()

len(books) # =>  2

books[0].id # =>  1
books[0].title # =>  'Nineteen Eighty-Four'
books[0].author_name # =>  'George Orwell'

books[1].id # =>  2
books[1].title # =>  'Mrs Dalloway'
books[1].author_name # => 'Virginia Woolf'

# app.py

book_repo = BookRepository(connection)
books = book_repo.all()

for book in books:
    print(book)


```