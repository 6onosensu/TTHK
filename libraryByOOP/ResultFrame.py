import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from BaseLabel import BaseLabel
from tables.Book import Book


class ResultFrame(tk.Frame):
    """
    A Frame for displaying search results or all records in the library application.
    """
    def __init__(self, parent, app, db_manager, *args, **kwargs):
        super().__init__(parent, bg="#290700", *args, **kwargs)
        self.app = app
        self.db_manager = db_manager
        self.init_widgets()

    def init_widgets(self):
        BaseLabel(self, text="Search results or Show All records by table:").pack(pady=0)
        self.columns = {"ID": 40, "Title": 400, "Pages": 100, "A ID": 40,
                        "Author": 200, "G ID": 40, "Genre": 200}
        self.tree = ttk.Treeview(self, columns=list(self.columns.keys()), show="headings")

        for col, width in self.columns.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width)

        self.tree.pack(expand=True, fill='both')

    def update_treeview(self, records):
        # Clear the current view
        for i in self.tree.get_children():
            self.tree.delete(i)
        # Insert new records
        for record in records:
            self.tree.insert('', 'end', values=record)
            print(record)

    def show_all_records(self, table="books"):
        records = self.db_manager.fetch_records(table)
        self.update_treeview(records)
