import sqlite3
from sqlite3 import Error

class DataManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = self.create_connection()

    def create_connection(self):
        try:
            return sqlite3.connect(self.db_path)
        except Error as e:
            print(f"An error occurred: {e}")
    
    def create_tables(self):
        create_authors_table = """
        CREATE TABLE IF NOT EXISTS authors(
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_name TEXT NOT NULL
        );
        """
        create_genres_table = """
        CREATE TABLE IF NOT EXISTS genres(
        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
        genre_name TEXT NOT NULL
        );
        """
        create_books_table = """
        CREATE TABLE IF NOT EXISTS books(
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        num_of_pages INTEGER,
        author_id INTEGER,
        genre_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(author_id),
        FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
        );
        """
        self.execute_query(create_authors_table)
        self.execute_query(create_genres_table)
        self.execute_query(create_books_table)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def show_all_records(self, table):
        query = f"SELECT * FROM {table}"
        return self.fetch_records(query)

    def add_record(self, table, **fields):
        columns = ', '.join(fields.keys())
        placeholders = ', '.join('?' for _ in fields)
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(fields.values()))

    def delete_record_by_id(self, table, id):
        query = f"DELETE FROM {table} WHERE id = ?"
        self.execute_query(query, (id,))
        print(f"Record with id {self.id} from table {table} has been deleted.")

    def update_record_by_id(self, table, id, updates):
        update_clause = ', '.join(f"{k} = ?" for k in updates.keys())
        query = f"UPDATE {table} SET {update_clause} WHERE id = ?"
        params = tuple(updates.values()) + (id,)
        try:
            self.execute_query(query, params)
            print(f"Record with id {self.id} from table {table} has been updated.")
        except Exception as e:
            print(f"An error occured: {e}")

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params or ())
            self.conn.commit()
        except Error as e:
            print(f"An error occurred: {e}")

    def fetch_records(self, table, condition=None):
        query = f"SELECT * FROM {table}"
        params = ()
        if condition:
            query += f" WHERE {condition[0]}"
            params = condition[1]
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def search_records(self, search_query):
        query = """
        SELECT books.id, books.title, books.pages_number, 
        authors.author_name, authors.author_id, 
        genre.genre_name, genre.genre_id
        FROM books
        JOIN authors ON books.author_id = authors.author_id
        JOIN genre ON books.genre_id = genre.genre_id
        WHERE books.title LIKE ? OR authors.author_name LIKE ? OR genre.genre_name LIKE ?
        """
        try:
            cursor = self.conn.cursor()
            # The same search query is used for all three conditions; adjust as necessary
            search_term = f'%{search_query}%'
            cursor.execute(query, (search_term, search_term, search_term))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list in case of an error
        