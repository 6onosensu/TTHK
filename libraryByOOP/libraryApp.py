from tkinter import *
from dataManager import *

class LibraryApp(Tk):
    def __init__(self, db_path):
        super().__init__()
        self.title("Welcome to the Library!")
        self.geometry("1000x600")
        self.configure(background='#290700')
        self.db_manager = DataManager(db_path)
        self.init_frames()

    def init_frames(self):
        self.search_frame = SearchFrame(self)
        self.search_frame.pack(pady=10)

    def run(self):
        self.mainloop()

class SearchFrame(Frame):
    def __init__(self, master, db_manager):
        super().__init__(master, bg='#290700')
        self.db_manager = db_manager
        
        self.search_text = StringVar()
        self.init_widgets()

    def init_widgets(self):
        Label(self, text="What can I help you find?", font="Arial 20", fg="#E8D8D6", bg='#290700').pack(pady=0)
        
        search_entry = Entry(self, font='Arial 20', width=80, textvariable=self.search_text, bg="#E8D8D6", fg="#290700")
        search_entry.pack(side=LEFT, padx=40, pady=10)
        search_entry.bind('<Return>', self.searching)
    
    def searching(self, event=None):
        search_query = self.search_text.get().strip()