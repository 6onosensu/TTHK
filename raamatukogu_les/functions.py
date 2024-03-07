from tkinter import *
from sqlite3 import *
from sqlite3 import Error
    
def instant_search(source, search_in, update_widget, parent_widget, search_text):
    txt = search_text.get.strip().lower()
    for widget in parent_widget.winfo_child():
        if isinstance(widget, Label) and "Search by query:" in widget.cget("text"):
            widget.destroy()

    search_label = Label(parent_widget, text=f"Search by query: {txt}",
                       font="Arial 24", fg="brown")
    search_label.pack(pady=5, padx=5)

    update_widget.delete(0, END)

    for item in source:
        if isinstance(source, list) and all(isinstance(item, dict)):
            for item in source:
                if txt in item[search_in].lower():
                    update_widget.insert(END, item[search_in])


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