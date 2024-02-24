from tkinter import *
import random

def txt_to_list(file):
    words = []
    file = open(file, "r", encoding="utf-8")
    for row in file:
        words.append(row.strip())
    return words

def create_entries(w):
    frame = Frame(root, bg='#9966CC')
    frame.pack(pady=20)
    entries = [[] for _ in range(max_attempts)]
    for a in range(max_attempts):
        for i in range(w):
            entry = Entry(frame, font='Arial 14', width=2, 
                          bg="#FAEBD7", justify='center')
            entry.grid(row=a, column=i, padx=5, pady=5)
            entries[a].append(entry)
        if a > 0:
            for entry in entries[a]:
                entry.config(state='disabled')
    return entries

def create_keyboard(rows):
    buttons = {}
    for _, row in enumerate(rows):
        row_frame = Frame(root, bg='#9966CC')
        row_frame.pack(side=TOP, pady=2)
        for letter in row:
            button = Button(row_frame, text=letter, width=2,
                            command=lambda l=letter: add_letter(l),
                            font='Arial 14', bg="#FAEBD7")
            button.pack(side=LEFT, padx=2)
            buttons[letter] = button
    submit_frame = Frame(root)
    submit_frame.pack(side=TOP, pady=2)
    submit_button = Button(submit_frame, text='Confirm', width=10, 
                           command=submit_guess, font='Arial 14',
                           bg="#FAEBD7")
    submit_button.pack(side=RIGHT, padx=2)
    return buttons

def add_letter(letter):
    global attempt, fields
    for field in fields[attempt]:
        if not field.get():
            field.insert(END, letter.upper())
            break

def submit_guess():
    global attempt, fields, word
    current_entries = fields[attempt]
    guess = ''.join(entry.get().lower() for entry in current_entries).capitalize()
    if len(guess) != word_len:
        return
    update_colors(current_entries, guess, word)
    is_win = guess == word
    if is_win or attempt == max_attempts - 1:
        end_game(is_win, word)
    else:
        attempt += 1
        if attempt < max_attempts:
            for entry in fields[attempt]:
                entry.config(state='normal')

def update_colors(fields, guess, word):
    for i, field in enumerate(fields):
        if word[i] == guess[i]:
            field.config(bg = "#3B7A57")
        elif guess[i] in word:
            field.config(bg = "#FFBF00")
        else:
            field.config(bg = "#FAEBD7")

def end_game(win, word):
    if win:
        rText = "Congratulations! You guessed the word!"
    else: 
        rText = f"The game is over. The word was: {word.upper()}."
    result_label.config(text=rText)

    for attempt_fields in fields:
        for field in attempt_fields:
            field.config(state='disabled')

first_row = "QWERTYUIOP"
second_row = "ASDFGHJKL"
third_row = "ZXCVBNM"
rows = [first_row, second_row, third_row]

root = Tk()
root.geometry("600x600")
root.title("Let's Play to Wordle!")
root.iconbitmap("word.ico")
root.configure(background='#9966CC')

lab = Label(root, text="Wordle-ENG", fg="#FAEBD7", font="Arial 20",
            height=1, bg="#9966CC")
lab.pack(pady=20)

words = txt_to_list("words.txt")
word = random.choice(words)
word_len = len(word)

max_attempts = 6
attempt = 0

fields = create_entries(word_len)
buttons = create_keyboard(rows)

result_label = Label(root, text="",  fg="#FAEBD7",
                     font = "Arial 14", bg='#9966CC')
result_label.pack(pady=20)

root.mainloop()


