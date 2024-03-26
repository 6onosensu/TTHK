import tkinter as tk
from tkinter import Tk
from DataManager import DataManager
from ResultFrame import ResultFrame
from SearchFrame import SearchFrame
from ActionsFrame import ActionsFrame

class LibraryApp(Tk):
    def __init__(self, db_path, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Welcome to the Library!")
        self.geometry("1030x600")
        self.configure(background='#290700')

        container = tk.Frame(self, bg='#290700')
        container.pack(padx=5, pady=5)
        
        self.db_manager = DataManager(db_path)
        self.db_manager.create_tables()
        self.frames = {}

        result_frame = ResultFrame(container, self, self.db_manager)
        self.frames[ResultFrame] = result_frame

        search_frame = SearchFrame(container, self, self.db_manager, result_frame)
        self.frames[SearchFrame] = search_frame

        actions_frame = ActionsFrame(container, self, self.db_manager)
        self.frames[ActionsFrame] = actions_frame

        for frame in self.frames.values():
            frame.pack(padx=5, pady=5)

        self.show_frame(SearchFrame)

    def show_frame(self, cont):
        '''Bring the frame of the given class to the top.'''
        frame = self.frames[cont]
        frame.tkraise()

    def run(self):
        self.mainloop()
