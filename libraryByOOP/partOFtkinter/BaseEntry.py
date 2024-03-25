from tkinter import Entry

class BaseEntry(Entry):
    def __init__(self, master, **kwargs):
        style = {
            'width': 65,
            'font': ("Arial", 20),
            'bg': '#E8D8D6',
            'fg': '#290700'
        }
        combined_style = {**style, **kwargs}
        super().__init__(master, **combined_style)