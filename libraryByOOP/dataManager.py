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

    def add_record(self, table, **fields):
        columns = ', '.join(fields.keys())
        placeholders = ', '.join('?' for _ in fields)
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(fields.values()))

    def delete_record(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query)

    def update_record(self, table, updates, condition):
        update_clause = ', '.join(f"{k} = ?" for k in updates.keys())
        query = f"UPDATE {table} SET {update_clause} WHERE {condition}"
        self.execute_query(query, tuple(updates.values()))

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params or ())
            self.conn.commit()
        except Error as e:
            print(f"An error occurred: {e}")

    def fetch_records(self, table, condition=None):
        query = f"SELECT * FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def search_books(self, search_query):
        query = """
        SELECT books.title, authors.author_name, genre.genre_name
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