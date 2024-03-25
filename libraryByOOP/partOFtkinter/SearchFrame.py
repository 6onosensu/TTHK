from libraryByOOP.partOFtkinter.BaseEntry import BaseEntry
from libraryByOOP.partOFtkinter.BaseLabel import BaseLabel
from libraryByOOP.partOFtkinter.BaseFrame import BaseFrame
from tkinter import *


class SearchFrame(BaseFrame):
    def init_widgets(self):
        super().init_widgets()
        BaseLabel(self, text="What can I help you find?").pack(pady=0)
        
        self.search_text = StringVar()
        search_entry = BaseEntry(self, textvariable=self.search_text)
        search_entry.pack(side=LEFT, padx=40, pady=10)
        search_entry.bind('<Return>', self.searching)
    
    def searching(self, event=None):
        search_query = self.search_text.get().strip()
        self.result_frame.show_search_results(search_query)