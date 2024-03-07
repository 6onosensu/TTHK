from functions import *
from tkinter import *
from tables import *
from os import *

filename = path.abspath(__file__)
db_directory = filename.rstrip('controller_lib.py')
db_path = path.join(db_directory, 'library.db')
connected = create_connection(db_path)


list_= [[create_authors_table, create_authors],
        [create_genre_table, create_genre],
        [create_books_table, create_books]]
for l in list_:
    for query in l:
        execute_query(connected, query)

books = execute_read_query(connected, select_books)
#print("The book data:")
#for book in books:
    #print(book)

#execute_delete_query(connected, delete_data_from_books)
#print("Deleted books, those with genre_id = 1")

#books = execute_read_query(connected, select_books)
#for book in books:
    #print(book)

# execute_read_query(connected, delete_table_books)

#add_author(connected, 'J.K. Rowling', '1965-07-31')
#add_genre(connected, 'fantasy')
#add_book(connected, 'Harry Potter and the Philosopher`s Stone', '1997-06-26', 6, 6)

#books = execute_read_query(connected, select_books)
#for book in books:
    #print(book)

#update_book(connected, book_id=8, title='New Title', publication_date='2022-01-01')
#books = execute_read_query(connected, select_books)
#for book in books:
    #print(book)

#delete_books_by_author(connected, author_id=1)
#delete_books_by_genre(connected, genre_id=1)



root = Tk()
root.geometry("1000x600")
root.title("Welcome to Database!")

lab = Label(root, text="Find what you need: ", font="Arial 24", fg="brown", height=1)
lab.pack(pady=20)

fram = Frame(root)
fram.pack(pady=5)
label_search = Label(fram, text="Search", font="Arial 24", fg="brown", height=1)
label_search.pack(pady=20, padx=10)
search_text = StringVar(fram)
entry_search = Entry(fram, font='Arial 14', width=60, textvariable=search_text)
entry_search.pack(padx=15)
listbox = Listbox(fram)
listbox.pack()
search_text.trace_add("write", lambda a, b, c: instant_search(books, 'name',
                      listbox, 'name', search_text))

root.mainloop()