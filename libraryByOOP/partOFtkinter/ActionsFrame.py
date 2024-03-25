from tkinter import *
from tkinter import messagebox
import libraryByOOP.partOFtkinter.BaseEntry as BaseEntry
from libraryByOOP.partOFtkinter.BaseLabel import BaseLabel
from libraryByOOP.partOFtkinter.BaseFrame import BaseFrame
from libraryByOOP.tables.Book import Book
from libraryByOOP.tables.Author import Author
from libraryByOOP.tables.Genre import Genre


class ActionsFrame(BaseFrame):
    def init_widgets(self):
        super().init_widgets()
        BaseLabel(self, text="ADD/DELETE/UPDATE/SHOW ALL").pack(pady=0)
        self.action_entry = BaseEntry(self)
        self.action_entry.pack(side=LEFT, padx=40, pady=10)
        self.create_buttons()

    def create_buttons(self):
        buttonsFrame = Frame(self, bg=self['bg'])
        buttonsFrame.pack(pady=5)
        self.actions = {
            'Add Author': self.add_author,
            'Add Book': self.add_book,
            'Add Genre': self.add_genre,
            'Update': self.update_record,
            'Delete': self.delete_record
        }
        for txtLab, command_ in self.actions.items():
            btn = Button(buttonsFrame, text=txtLab, command=command_,
                        width=10, bg="#E8D8D6", fg="#290700")
            btn.pack(side=RIGHT, padx=2)
    
    def show_error(self, error_txt):
        print(error_txt)
        messagebox.showerror("Error", error_txt) 


    def add_author(self):
        data = self.get_data()
        name = data.strip()
        
        author_adding = Author(self.db_manager.db_path, None, name)
        author_adding.add_author()

    def add_genre(self):
        data = self.get_data()
        name = data.strip()
        
        genre_adding = Genre(self.db_manager.db_path, None, name)
        genre_adding.add_genre()

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
            book_adding.add_book()
        else:
            self.show_error("Invalid input format.")

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
            """
            if toUpdate not in ["genre", "author", "book"]:
                self.show_error(f"Invalid record type for update: {toUpdate}")
                return

            try:
                id = int(data[1].strip())
                if toUpdate == "genre":
                    updates = {'genre_name': data[2].lower()}
                elif toUpdate == "author":
                    updates = {'author_name': data[2]}
                elif toUpdate == "book":
                    updates = {
                        'title': data[2],
                        'num_of_pages': int(data[3]),
                        'author_id': int(data[4]),
                        'genre_id': int(data[5])
                    }
                self.db_manager.update_record_by_id(f"{toUpdate}s", id, updates)
            except ValueError:
                self.show_error("id, num_of_pages, author_id, and genre_id must be numbers.")
            except IndexError:
                self.show_error("Not enough data provided for update.")
            """
        else:
            self.show_error("Not enough data provided for update.")
 
    def record_to_update(self, toUpdate, id):
        match toUpdate:
            case "genre":
                return Genre(self.db_manager.db_path, id)
            case "author":
                return Author(self.db_manager.db_path, id)
            case "book":
                return Book(self.db_manager.db_path, id)

    def get_data(self):
        return self.action_entry.get()

    def delete_record(self):
        data = self.get_data().split(", ")
        toDelete = data[0].strip().lower()
        id = int(data[1].strip())
        if toDelete in ["books", "authors", "genres"]:
            self.db_manager.delete_record_by_id(f"{toDelete}s", id)
        else:
            self.show_error("Invalid record type.")

