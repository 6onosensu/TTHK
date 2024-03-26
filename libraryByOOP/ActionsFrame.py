import tkinter as tk
from tkinter import messagebox
from BaseEntry import BaseEntry
from BaseLabel import BaseLabel
from tables.Book import Book
from tables.Author import Author
from tables.Genre import Genre


class ActionsFrame(tk.Frame):
    """
    A Frame for performing actions such as adding, deleting, or updating records.
    """
    def __init__(self, parent, app, db_manager, result_frame, *args, **kwargs):
        super().__init__(parent, bg="#290700", *args, **kwargs)
        self.app = app
        self.db_manager = db_manager
        self.init_widgets()
        self.result_frame = result_frame

    def init_widgets(self):
        BaseLabel(self, text="ADD/DELETE/UPDATE/SHOW ALL").pack(pady=0)
        self.action_entry = BaseEntry(self)
        self.action_entry.pack(padx=40, pady=10)
        self.create_buttons()

    def create_buttons(self):
        buttonsFrame = tk.Frame(self, bg='#290700')
        buttonsFrame.pack(pady=5)
        self.actions = {
            'Add Author': self.add_author,
            'Add Book': self.add_book,
            'Add Genre': self.add_genre,
            'Update': self.update_record,
            'Delete': self.delete_record,
            'Show Table': self.show_table
        }
        for txtLab, command_ in self.actions.items():
            btn = tk.Button(buttonsFrame, text=txtLab, command=command_,
                        width=10, bg="#E8D8D6", fg="#290700")
            btn.pack(side=tk.LEFT, padx=5, pady=0)

        self.show_hints()

    def show_hints(self):
        txt = """
            --Write a request and press the required button!--
            Adding book: title, number_of_pages, author_id, genre_id
            Adding author/Adding genre: author_name/genre_name
            Show all records in a table: table_name
            UPDATE: book/author/genre, book_id/author_id/genre_id, follow_the_order_of_adding
            DELETE: book/author/genre, book_id/author_id/genre_id
        """
        BaseLabel(self, text=txt, font="Arial 12").pack(padx=20, pady=5)
    
    def show_error(self, error_txt):
        print(error_txt)
        messagebox.showerror("Error", error_txt) 
    
    def get_data(self):
        return self.action_entry.get()

    def clear_entry(self):
        self.action_entry.delete(0, tk.END)

    def show_table(self):
        data = self.get_data().lower().strip()
        match data:
            case "genres":
                records = self.db_manager.fetch_records("genres")
            case "authors":
                records = self.db_manager.fetch_records("authors")
            case "books":
                records = self.db_manager.fetch_records("books")
            case _:
                records = []
                self.show_error("Invalid table name.")
        self.clear_entry()
        self.result_frame.update_treeview(records)
        for record in records:
            print(record)

    def add_author(self):
        data = self.get_data()
        name = data.strip()
        
        author_adding = Author(self.db_manager.db_path, None, name)
        author_adding.create()
        self.clear_entry()

    def add_genre(self):
        name = self.get_data().strip()
        
        genre_adding = Genre(self.db_manager.db_path, None, name)
        genre_adding.create()
        self.clear_entry()

    def add_book(self):
        data = self.get_data()
        book_data = data.split(", ")
        if len(book_data) == 4:
            try:
                title = book_data[0].strip()
                pages = int(book_data[1].strip())
                aID = int(book_data[2].strip())
                gID = int(book_data[3].strip())
            except ValueError:
                self.show_error("Please, ensure that 'pages', 'Author ID' and 'Genre ID' are numbers.")
            
            book_adding = Book(self.db_manager.db_path, None, title, pages, aID, gID)
            book_adding.create()
        else:
            self.show_error("Invalid input format.")
        self.clear_entry()

    def update_record(self):
        data = self.get_data().split(", ")
        if len(data) >= 3:
            toUpdate = data[0].strip()
            id = int(data[1].strip())
            record = self.record_to_update(toUpdate, id)
            record.name = data[2]
            if data[3]:
                record.num_of_pages = int(data[3])
            if data[4]:
                record.author_id = int(data[4])
            if data[5]:
                record.genre_id = int(data[5])
            record.update()
        else:
            self.show_error("Not enough data provided for update.")
        self.clear_entry()
 
    def record_to_update(self, toUpdate, id):
        match toUpdate:
            case "genre":
                return Genre(self.db_manager.db_path, id)
            case "author":
                return Author(self.db_manager.db_path, id)
            case "book":
                return Book(self.db_manager.db_path, id)

    def delete_record(self):
        data = self.get_data().split(", ")
        toDelete = data[0].strip().lower()
        id = int(data[1].strip())
        if toDelete in ["books", "authors", "genres"]:
            self.db_manager.delete_record_by_id(f"{toDelete}s", id)
        else:
            self.show_error("Invalid record type.")
        self.clear_entry()
