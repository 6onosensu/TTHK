from sqlite3 import *
from sqlite3 import Error

def create_connection(path: str):
    connection = None
    try:
        connection = connect(path)
        print("Uhendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga '{e}'")
    return connection

def execute_query(connection, query: str):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Table is created")
    except Error as e:
        print(f"Error '{e}' with creating the table")
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
    ('The World War I','2004-01-1',5),
    ('The World War II','2005-02-2',1),
    ('The World War III','2006-03-3',4),
    ('She','2024-02-29',2),
    ('Dr. Stanny','1998-12-09',3);
"""

select_users = "SELECT * FROM books"
#----------------------------------------------------------------

connected = create_connection("C:/Users/opilane/Desktop/TTHK/json_database/appData/raamatukogu/data.db")
list_= [[create_authors_table, create_authors], [create_genre_table, create_genre], [create_books_table, create_books]]
for l in list_:
    for query in l:
        execute_query(connected, query)
