from game import *

first_row = "QWERTYUIOP"
second_row = "ASDFGHJKL"
third_row = "ZXCVBNM"
rows = [first_row, second_row, third_row]

entries = []
buttons = []

def txt_to_list(file):
    words = []
    file = open(file, "r", encoding="utf-8")
    for row in file:
        words.append(row.strip())
    file.close()
    return words

def random_word(words: list):
    pass

def create_entries(word):
    for i in range(len(word)):
        entry = Entry(root, width=2, font='Arial 14')
        entry.grid(row=0, column=i, padx=5, pady=40)
        entries.append(entry)

def add_letter(letter):
    for entry in entries:
        if not entry.get():
            entry.insert(0, letter)
            break

def create_buttons():
    for r in range(len(rows)):
        for index, letter in enumerate(r):
            button = Button(root, text=letter, bg="gray",
            command=lambda l=letter: add_letter(l),
            width=2, font='Arial 14').grid(row=1)