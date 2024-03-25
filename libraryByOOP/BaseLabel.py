from tkinter import Label

class BaseLabel(Label):
    def __init__(self, master, **kwargs):
        style = {
            'font': ("Arial", 20),
            'bg': '#290700',
            'fg': '#E8D8D6'
        }
        combined_style = {**style, **kwargs}
        super().__init__(master, **combined_style)