import tkinter as tk
from tkinter import ttk
from BaseLabel import BaseLabel


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
        c_keys = self.columns.keys()
        list_of_keys = list(c_keys)
        self.tree = ttk.Treeview(self, columns=list_of_keys, show="headings")

        for heading, w in self.columns.items():
            self.tree.heading(heading, text=heading)
            self.tree.column(heading, width=w)
        self.tree.pack(pady=5)
        

    def update_treeview(self, records):
        # Clear the current view
        for i in self.tree.get_children():
            self.tree.delete(i)
        # Insert new records
        for record in records:
            self.tree.insert('', 'end', values=record)

    def show_all_records(self):
        records = self.db_manager.fetch_records("books")
        self.update_treeview(records)

    def show_search_results(self, search_query):
        records = self.db_manager.search_records(search_query)
        self.update_treeview(records)
