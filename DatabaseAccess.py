import sqlite3
from sqlite3 import Error

class DatabaseAccess:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = self.create_connection()

    def create_connection(self):
            try:
                conn = sqlite3.connect(self.db_path)
                return conn
            except Error as e:
                print(f"An error occurred '{e}'")

    def execute_query(self, query, parameters=None):
        cursor = self.connection.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        self.connection.commit()



    def get_books(self):
        query = "SELECT * FROM book"
        return self.execute_query(query)

    def add_book(self, title, publication_date, genre_id, author_id):
        query = "INSERT INTO book (title, publication_date, genre_id, author_id) VALUES (?, ?, ?, ?)"
        self.execute_query(query, (title, publication_date, genre_id, author_id))