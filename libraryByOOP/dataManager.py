import sqlite3
from sqlite3 import Error

class DataManager:
    table_name = ""
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
        author_name TEXT,
        genre_id INTEGER,
        genre_name TEXT,
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

    def add_record(self, **fields):
        columns = ', '.join(fields.keys())
        placeholders = ', '.join('?' for _ in fields)
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(fields.values()))

    def delete_record_by_id(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.execute_query(query, (id,))
        print(f"Record with id {self.id} from table {self.table_name} has been deleted.")

    def update_record_by_id(self, id, updates):
        update_clause = ', '.join(f"{k} = ?" for k in updates.keys())
        query = f"UPDATE {self.table_name} SET {update_clause} WHERE id = ?"
        params = tuple(updates.values()) + (id,)
        try:
            self.execute_query(query, params)
            print(f"Record with id {self.id} from table {self.table_name} has been updated.")
        except Exception as e:
            print(f"An error occured: {e}")

    def fetch_records(self, condition=None): #show_table_records
        query = f"SELECT * FROM {self.table_name}"
        if condition:
            query += f" WHERE {condition}"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params or ())
            self.conn.commit()
            print(f"The query request was successful!")
        except Error as e:
            print(f"An error occurred: {e}")

    def search_records(self, search_query):
        query = """
        SELECT b.book_id, b.title, b.num_of_pages, 
               a.author_id, a.author_name, 
               g.genre_id, g.genre_name
        FROM books AS b
        JOIN authors AS a ON b.author_id = a.author_id
        JOIN genres AS g ON b.genre_id = g.genre_id
        WHERE b.title LIKE ? OR a.author_name LIKE ? OR g.genre_name LIKE ?
        """
        try:
            cursor = self.conn.cursor()
            # The same search query is used for all three conditions; adjust as necessary
            search_term = '%' + search_query + '%'
            cursor.execute(query, (search_term, search_term, search_term))
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []
