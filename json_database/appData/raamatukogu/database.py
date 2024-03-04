from sqlite3 import *
from sqlite3 import Error

def create_connection(path: str):
    connection = None
    try:
        connection = connect(path)
        print("The connection has been successfully made.")
    except Error as e:
        print(f"An error occurred '{e}'")
    return connection

def execute_query(connection, query: str):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error '{e}' with creating the table")

def execute_read_query(connection, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error '{e}'")

def execute_delete_query(connection, query: str):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("The table/data has been deleted.")
    except Error as e:
        print(f"Error '{e}'")

def add_author(connection, author_name, date_of_birth):
    query = f"""
    INSERT INTO authors(author_name, date_of_birth)
    VALUES('{author_name}', '{date_of_birth}');
    """
    execute_query(connection, query)

def add_genre(connection, genre_name):
    query = f"""
    INSERT INTO genre(genre_name)
    VALUES('{genre_name}');
    """
    execute_query(connection, query)

def add_book(connection, title, publication_date, author_id, genre_id):
    query = f"""
    INSERT INTO books(title, publication_date, author_id, genre_id)
    VALUES('{title}', '{publication_date}', {author_id}, {genre_id});
    """
    execute_query(connection, query)

def update_book(connection, book_id, title=None, publication_date=None, author_id=None, genre_id=None):
    updates = []
    if title:
        updates.append(f"title = '{title}'")
    if publication_date:
        updates.append(f"publication_date = '{publication_date}'")
    if author_id:
        updates.append(f"author_id = {author_id}")
    if genre_id:
        updates.append(f"genre_id = {genre_id}")

    if updates:
        set_clause = ", ".join(updates)
        query = f"""
        UPDATE books
        SET {set_clause}
        WHERE book_id = {book_id};
        """
        execute_query(connection, query)
    else:
        print("No updates provided.")

def delete_books_by_author(connection, author_id):
    query = f"""
    DELETE FROM books
    WHERE author_id = {author_id};
    """
    execute_query(connection, query)

def delete_books_by_genre(connection, genre_id):
    query = f"""
    DELETE FROM books
    WHERE genre_id = {genre_id};
    """
    execute_query(connection, query)

#----------------------------------------------------------------
create_authors_table = """
CREATE TABLE IF NOT EXISTS authors(
author_id INTEGER PRIMARY KEY AUTOINCREMENT,
author_name TEXT NOT NULL,
date_of_birth DATE
);
"""
create_genre_table = """
CREATE TABLE IF NOT EXISTS genre(
genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
genre_name TEXT NOT NULL
);
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS books(
book_id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
publication_date DATE,
author_id INTEGER,
genre_id INTEGER,
FOREIGN KEY (author_id) REFERENCES authors(author_id),
FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);
"""


create_authors = """
INSERT INTO 
    authors(author_name,date_of_birth)
VALUES
    ('Timmy Birtly','1989-12-31'),
    ('Don Santos','1999-01-01'),
    ('Tyrion Lannister','1995-10-16'),
    ('Leah','1988-08-18'),
    ('Billy Bom','2015-05-21');
"""
create_genre = """
INSERT INTO 
    genre(genre_name)
VALUES
    ('horror'),
    ('fiction'),
    ('rom-com'),
    ('folklore'),
    ('historical');
"""
create_books = """
INSERT INTO 
    books(title,publication_date,author_id,genre_id)
VALUES
    ('The World War I','2004-01-1',5, 1),
    ('The World War II','2005-02-2',1, 2),
    ('The World War III','2006-03-3',4, 3),
    ('She','2024-02-29',2, 4),
    ('Dr. Stanny','1998-12-09',3, 5);
"""

select_books = "SELECT * FROM books"

delete_data_from_books = "DELETE FROM books WHERE genre_id=1"

delete_table_books = "DROP TABLE books"
#----------------------------------------------------------------

# connected = create_connection("C:/Users/opilane/Desktop/TTHK/json_database/appData/raamatukogu/data.db")
connected = create_connection("C:/work/TTHK/json_database/appData/raamatukogu/data.db")

list_= [[create_authors_table, create_authors], [create_genre_table, create_genre], [create_books_table, create_books]]
for l in list_:
    for query in l:
        execute_query(connected, query)

books = execute_read_query(connected, select_books)
print("The book data:")
for book in books:
    print(book)

execute_delete_query(connected, delete_data_from_books)
print("Deleted books, those with genre_id = 1")

books = execute_read_query(connected, select_books)
for book in books:
    print(book)

# execute_read_query(connected, delete_table_books)

add_author(connected, 'J.K. Rowling', '1965-07-31')
add_genre(connected, 'fantasy')
add_book(connected, 'Harry Potter and the Philosopher`s Stone', '1997-06-26', 6, 6)

books = execute_read_query(connected, select_books)
for book in books:
    print(book)

update_book(connected, book_id=8, title='New Title', publication_date='2022-01-01')
books = execute_read_query(connected, select_books)
for book in books:
    print(book)

#delete_books_by_author(connected, author_id=1)
#delete_books_by_genre(connected, genre_id=1)