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

select_books = "SELECT * FROM books"

delete_data_from_books = "DELETE FROM books WHERE genre_id=1"

delete_table_books = "DROP TABLE books"


