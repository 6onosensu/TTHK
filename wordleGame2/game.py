from tkinter import *
import random

def txt_to_list(file):
    words = []
    file = open(file, "r", encoding="utf-8")
    for row in file:
        words.append(row.strip())
    return words

def create_entries(word):
    entries = []
    for i in range(len(word)):
        entry = Entry(root, font='Arial 14', width=2, justify='center')
        entry.grid(row=0, column=i, padx=5, pady=40)
        entries.append(entry)
    return entries

def add_letter(letter):
    for entry in entries:
        if not entry.get():
            entry.insert(0, letter)
            break

def create_buttons():
    buttons = []
    for r in range(len(rows)):
        for index, letter in enumerate(rows[r]):
            button = Button(root, text=letter, bg="gray",
            command=lambda l=letter: add_letter(l),
            width=2, font='Arial 14')
            button.grid(row=r+1, column=index)
            buttons.append(button)
    return button

def submit_guess():
    global attempt, entries
    guess = ''.join(entry.get() for entry in entries)

    if attempt < max_attempts:
        update_colors(entries, guess)
        attempt += 1
    if guess == target_word or attempt == max_attempts:
        end_game(guess == target_word)

def end_game(win):
    for entry in entries:
        entry.config(state='disabled')
    for button in buttons:
        button.config(state='disabled')
    result_label.config(text="Congrats! You are the winner!" if win else f"Game is finished. The word was '{target_word.upper()}'.")


def update_colors(entries, guess):
    for i in range(len(guess)):
        char = guess[i]
        if target_word[i] == char:
            entries[i].config(bg = "green")
        elif char in target_word:
            entries[i].config(bg = "yellow")
        else:
            entries[i].config(bg = "red")



root = Tk()
root.geometry("600x600")
root.title("Let's Play to Wordle!")
root.iconbitmap("word.py")
root.configure(background='darkblue')

lab = Label(root, text="Wordle-ENG", fg="white", font="Arial 20",
            height=1, bg="darkblue")
lab.pack(pady=20)

words_frame = Frame(root)
words_frame.pack(pady=40)


first_row = "QWERTYUIOP"
second_row = "ASDFGHJKL"
third_row = "ZXCVBNM"
rows = [first_row, second_row, third_row]

words = txt_to_list("words.txt")
target_word = random.choice(words)

max_attempts = 6
attempt = 0

entries = create_entries(target_word, words_frame)
buttons = create_buttons(words_frame)

submit_button = Button(root, text="confirm", command=submit_guess)
submit_button.pack(pady=20)

result_label = Label(root, text="", font = "Arial 14")
result_label.pack(pady=20)

root.mainloop()


