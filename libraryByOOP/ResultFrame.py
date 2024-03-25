from tkinter import *
from tkinter import ttk
from BaseLabel import BaseLabel
from BaseFrame import BaseFrame


class ResultFrame(BaseFrame):
    def init_widgets(self):
        BaseLabel(self, text="Search results or Show All records by table:").pack(pady=0)
        self.columns = ("ID", "Title", "Num of Pages", "Author ID", "Author",
                        "Genre ID", "Genre")
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")
        self.tree.pack(pady=5)

    def update_treeview(self, records):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for record in records:
            self.tree.insert('', 'end', values=record)

    def show_all_records(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        records = self.db_manager.fetch_records("books")
        for record in records:
            self.tree.insert('', 'end', values=record)

    def show_search_results(self, search_query):
        records = self.db_manager.search_records(search_query)
        self.update_treeview(records)
