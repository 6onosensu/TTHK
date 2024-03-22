from tkinter import *
from tkinter import ttk
from functions import *
from os import path
from tables import *

filename = path.abspath(__file__)
db_directory = filename.rstrip('controller_lib.py') 
db_path = path.join(db_directory, 'library.db')
conn = create_connection(db_path)

# for creating tables and their initial filling
#list_ = [[create_authors_table, create_authors],
#         [create_genre_table, create_genre],
#         [create_books_table, create_books]]
#for l in list_:
#    for query in l:
#        execute_query(conn, query)

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

def createButtons(frame):
    buttonsFrame = Frame(frame, bg='#290700')
    buttonsFrame.pack(pady=5)
    buttons = {'Add Author': get_entry_author,
            'Add Book': get_entry_book,
            'Add Genre': get_entry_genre(),
            'Delete': get_dataToDelete}

    for txtLab, command_ in buttons.items():
        btn = Button(buttonsFrame, text=txtLab, command=command_,
                    width=10, bg="#E8D8D6", fg="#290700")
        btn.pack(side=RIGHT, padx=2)

def get_entry_book():
    global conn, welcomeFrame
    data = addDelete_Entry.get()
    book = data.split(", ")
    title = book[0].strip()
    pubDate = book[1].strip()
    aID = book[2].strip()
    gID = book[3].strip()
    add_book(conn, welcomeFrame, title, pubDate, aID, gID)

def get_entry_genre():
    global conn, welcomeFrame
    data = addDelete_Entry.get()
    name = data.strip()
    add_genre(conn, welcomeFrame, name)

def get_entry_author():
    global conn, welcomeFrame
    data = addDelete_Entry.get()
    a = data.split(", ")
    name = a[0].strip()
    birth = a[1].strip()
    add_author(conn, welcomeFrame, name, birth)

def get_dataToDelete():
    global conn, welcomeFrame
    data = addDelete_Entry.get()
    what = data[0].strip()
    id = data[1].strip()
    deleteData(conn, welcomeFrame, what, id)

root = Tk()
root.geometry("1000x600")
root.title("Welcome to the Library!")
root.configure(background='#290700')

frames = create_frames(root)
# -------------------------------------------------------------------------------------------------
welcomeFrame = Frame(root, bg='#290700')
welcomeFrame.pack(pady=10)

welcomeLab = Label(welcomeFrame, text="What can I help you find?",
                    font="Arial 20", fg="#E8D8D6", bg='#290700')
welcomeLab.pack(pady=0)

search_text = StringVar()
searchEntry = Entry(welcomeFrame, font='Arial 20', width=80,
                    textvariable=search_text, bg="#E8D8D6", fg="#290700")
searchEntry.pack(side=LEFT, padx=40, pady=10)
searchEntry.bind('<Return>', searching) # 

# -----------------------------------------------------------------------------------------------
resultFrame = Frame(root, bg='#290700')
resultFrame.pack(pady=0)
resultLab = Label(resultFrame, text="Search results:", font="Arial 20",
                    fg="#E8D8D6", bg='#290700', height=1)
resultLab.pack(pady=0)

# Treeview - to display search results with sorting options
columns = ("Title", "Author", "Genre")
tree = ttk.Treeview(resultFrame, columns=columns, show="headings")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author") # properties of the heading
tree.heading("Genre", text="Genre")
tree.column("Title", width=400) # properties of the column
tree.column("Author", width=300)
tree.column("Genre", width=200)
tree.pack(pady=5)

# -------------------------------------------------------------------------------------------------
updateBDFrame = Frame(root, bg='#290700')
updateBDFrame.pack(pady=0)
addDeleteLab = Label(updateBDFrame, text="ADD/DELETE", font="Arial 20",
                    fg="#E8D8D6", bg='#290700')
addDeleteLab.pack(pady=5)
addDelete_Entry = Entry(updateBDFrame, font='Arial 20', width=50,
                        bg="#E8D8D6", fg="#290700")
addDelete_Entry.pack(padx=40, pady=5)



mistakeFrame = Frame(updateBDFrame, bg='#290700')
mistakeFrame.pack(pady=0)

created_buttons = createButtons(updateBDFrame)

txt = """
Adding book: title, publication_date, author_id, genre_id
Adding author: author_name, date_of_birth
Adding genre: genre_name
Delete: book/author/genre, book_id/author_id/genre_id"""
hintLab = Label(updateBDFrame, text="Writing hints are provided here:", font="Arial 20", fg="#E8D8D6", bg='#290700', height=1)
hintLab.pack(pady=0)
hintValueLab = Label(updateBDFrame, text=txt, font="Arial 16", fg="#E8D8D6", bg='#290700')
hintValueLab.pack(pady=0)


root.mainloop()