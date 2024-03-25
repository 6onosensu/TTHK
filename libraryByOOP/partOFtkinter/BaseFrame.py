from tkinter import Frame
from LibraryApp import *

class BaseFrame(Frame):
    def __init__(self, master, db_manager, result_frame=None, bg='#290700', **kwargs):
        super().__init__(master, bg=bg, **kwargs)
        self.db_manager = db_manager
        self.result_frame = result_frame
        self.init_widgets()

    def init_frames(self):
        self.result_frame = ResultFrame(self.master, self.db_manager)
        self.result_frame.pack(pady=10)
        self.search_frame = SearchFrame(self.master, self.db_manager, self.result_frame)
        self.search_frame.pack(pady=10)
        self.actions_frame = ActionsFrame(self.master, self.db_manager, self.result_frame)
        self.actions_frame.pack(pady=10)

    def init_widgets(self):
        pass
    