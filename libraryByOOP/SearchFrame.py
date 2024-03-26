from BaseEntry import BaseEntry
from BaseLabel import BaseLabel
import tkinter as tk


class SearchFrame(tk.Frame):
    """
    A Frame for searching within the library application.

    Parameters:
    - parent: The parent widget.
    - app: Reference to the main application instance.
    - db_manager: The database manager for handling database operations.
    - result_frame: The frame where search results should be displayed.
    """
    def __init__(self, parent, app, db_manager, result_frame, *args, **kwargs):
        super().__init__(parent, bg="#290700", *args, **kwargs)
        self.app = app
        self.db_manager = db_manager
        self.init_widgets()
        self.result_frame = result_frame

    def init_widgets(self):
        BaseLabel(self, text="What can I help you find?").pack(pady=0)
        
        self.search_text = tk.StringVar()
        search_entry = BaseEntry(self, textvariable=self.search_text)
        search_entry.pack(pady=10)
        search_entry.bind('<Return>', self.searching)
    
    def searching(self, event=None):
        search_query = self.search_text.get().strip()
        self.result_frame.show_search_results(search_query)