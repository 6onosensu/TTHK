from tkinter import *
from tkinter import ttk
from functions import *
import sqlite3
from os import path
from tables import *

filename = path.abspath(__file__)
db_directory = filename.rstrip('controller_lib.py') 
db_path = path.join(db_directory, 'library.db')
conn = create_connection(db_path)

# for creating tables and their initial filling
list_ = [[create_authors_table, create_authors],
         [create_genre_table, create_genre],
         [create_books_table, create_books]]
for l in list_:
    for query in l:
        execute_query(conn, query)

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

def searching(event=None):
    search_query = search_text.get().strip()
    # tree - a widget "treeview" used for showing the results.
    for i in tree.get_children():  # get_children returns a list of all rows in Treeview
        tree.delete(i) # cleaning before!
    books = fetch_books(conn, search_query) # returns tuples with results
    for book in books:
        tree.insert('', 'end', values=(book[0], book[1], book[2])) # ''- row adds to the root of treeview,
        # 'end' - row must be added in the enfd of the list
        # takes a tuple with data to display in the row.
        # book[0], book[1], and book[2] represent the title of the book, the author's name, and the genre.

root = Tk()
root.geometry("1000x600")
root.title("Welcome to the Library!")
root.configure(background='#290700')

welcomeFrame = Frame(root, bg='#290700')
welcomeFrame.pack(pady=20)

welcomeLab = Label(welcomeFrame, text="What can I help you find?", font="Arial 24", fg="#E8D8D6", bg='#290700', height=1)
welcomeLab.pack(pady=20)

search_text = StringVar()
searchEntry = Entry(welcomeFrame, font='Arial 20', width=80, textvariable=search_text, bg="#E8D8D6", fg="#290700")
searchEntry.pack(side=LEFT, padx=40, pady=10)
searchEntry.bind('<Return>', searching) # 


resultFrame = Frame(root, bg='#290700')
resultFrame.pack(pady=10)
resultLab = Label(resultFrame, text="Search results:", font="Arial 24", fg="#E8D8D6", bg='#290700', height=1)
resultLab.pack(pady=0)

# Treeview - to display search results with sorting options
columns = ("Title", "Author", "Genre")
tree = ttk.Treeview(resultFrame, columns=columns, show="headings")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author") # properties of the heading
tree.heading("Genre", text="Genre")
tree.column("Title", width=200) # properties of the column
tree.column("Author", width=150)
tree.column("Genre", width=100)
tree.pack(pady=20)

root.mainloop()