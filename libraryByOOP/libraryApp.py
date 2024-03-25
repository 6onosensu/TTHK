from tkinter import Tk
from DataManager import DataManager
from BaseFrame import BaseFrame
from ResultFrame import ResultFrame
from SearchFrame import SearchFrame
from ActionsFrame import ActionsFrame

class LibraryApp(Tk):
    def __init__(self, db_path):
        root = super().__init__()
        self.title("Welcome to the Library!")
        self.geometry("1000x600")
        self.configure(background='#290700')
        self.db_manager = DataManager(db_path)
        self.init_frame = BaseFrame(root, self.db_manager)
        self.init_frame.init_frames()
        self.init_frame.pack(pady=0, padx=5)

    def run(self):
        self.mainloop()
