from cProfile import label
from tkinter import *
from sqlite3 import *
import sqlite3
from sqlite3 import Error

def create_connection(path: str):
    conn = None
    try:
        conn = connect(path)
        print("The connection has been successfully made.")
    except Error as e:
        print(f"An error occurred '{e}'")
    return conn

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

def add_author(connection, fram, author_name, date_of_birth):
    query = f"""
    INSERT INTO authors(author_name, date_of_birth)
    VALUES('{author_name}', '{date_of_birth}');
    """
    execute_query(connection, query)
    success(fram)

def add_genre(connection, fram, genre_name):
    query = f"""
    INSERT INTO genre(genre_name)
    VALUES('{genre_name}');
    """
    execute_query(connection, query)
    success(fram)

def add_book(connection, fram, title, publication_date, author_id, genre_id):
    query = f"""
    INSERT INTO books(title, publication_date, author_id, genre_id)
    VALUES('{title}', '{publication_date}', {author_id}, {genre_id});
    """
    execute_query(connection, query)
    success(fram)

def success(fram):
    successed = Label(fram, text="Successfully added", fg="#E8D8D6", bg='#290700', font="Arial 20")
    successed.pack(padx=40, pady=2)

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


def fetch_books(conn, search_query):
    try:
        cursor = conn.cursor() # For executing queries
        query = """
        SELECT books.title, authors.author_name, genre.genre_name 
        FROM books
        JOIN authors ON books.author_id = authors.author_id
        JOIN genre ON books.genre_id = genre.genre_id
        WHERE books.title LIKE ?
        """
        cursor.execute(query, ('%' + search_query + '%',))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return [] # return empty only if an error

def deleteData(connection, param):
    param = param.split(", ")
    toDelete = param[0].strip().lower()
    id = param[1].strip()
    if toDelete == "book":
        pass
    elif toDelete == "author":
        pass
    elif toDelete == "genre":
        pass
    else:
        ifError(toDelete, id)

# ----------------------------------------------------------------------
# nado obdumat!
def create_frames(root):
    frames = {'welcomeFrame': root,
            'resultFrame': root,
            'updateBDFrame': root}
    for varName, place in frames.items():
        varName = Frame(place, bg='#290700')
        varName.pack(pady=5)

def ifError(frame, yourInput):
    mistake = "Somewhere there might have been a mistake:\n" + yourInput
    allErrors = Label(frame, text=mistake, font="Arial 20",
                        fg="#E8D8D6", bg='#290700')
    allErrors.pack(padx=40, pady=2)