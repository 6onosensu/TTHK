import tkinter as tk
import random

def txt_to_list(file):
    words = []
    with open(file, "r", encoding="utf-8") as f:
        words = f.read().splitlines()
    return words

def create_entries(parent, word_length):
    return [tk.Entry(parent, font='Arial 14', bg='#FFD300', width=2, justify='center') for _ in range(word_length)]

def create_keyboard(parent, letters):
    buttons = {}
    for letter in letters:
        button = tk.Button(parent, text=letter, bg='#FFD300', width=2, command=lambda l=letter: add_letter(l))
        buttons[letter] = button
    return buttons

def add_letter(letter):
    for entry in entries:
        if not entry.get():
            entry.insert(tk.END, letter.upper())
            break
    if all(entry.get() for entry in entries):
        check_guess()

def check_guess():
    global attempt
    guess = ''.join(entry.get().lower() for entry in entries)
    if guess == target_word:
        for entry in entries:
            entry.config(bg='green')
        end_game(True)
    else:
        for i, entry in enumerate(entries):
            if guess[i] == target_word[i]:
                entry.config(bg='green')
            elif guess[i] in target_word:
                entry.config(bg='yellow')
            else:
                entry.config(bg='red')
    attempt += 1
    if attempt >= max_attempts:
        end_game(False)
    for entry in entries:
        entry.delete(0, tk.END)

def end_game(win):
    result_label.config(text="Congtrats, you win!!" if win else f"The game finished. The word was {target_word.upper()}.")
    for button in keyboard.values():
        button.config(state='disabled')

first_row = "QWERTYUIOP"
second_row = "ASDFGHJKL"
third_row = "ZXCVBNM"
rows = [first_row, second_row, third_row]

root = tk.Tk()
root.geometry("600x600")
root.title("Let's Play to Wordle!")
root.configure(background='#FFD300')

lab = tk.Label(root, text="Wordle-ENG", fg="white", font="Arial 20",
            height=1, bg="#FFD300")
lab.pack(pady=20)

words_frame = tk.Frame(root, bg='#FFD300')
words_frame.pack(pady=20)

keyboard_frame = tk.Frame(root, bg='#FFD300')
keyboard_frame.pack(pady=20)

words = txt_to_list("words.txt")
target_word = random.choice(words)

max_attempts = 6
attempt = 0

entries = create_entries(words_frame, len(target_word))
keyboard = create_keyboard(keyboard_frame, ''.join(rows))

for i, entry in enumerate(entries):
    entry.grid(row=0, column=i, padx=5, pady=5)
for i, row in enumerate(rows):
    for j, letter in enumerate(row):
        button = keyboard[letter]
        button.grid(row=i, column=j, padx=5, pady=5)


result_label = tk.Label(root, text="", font="Arial 14")
result_label.pack(pady=20)

root.mainloop()