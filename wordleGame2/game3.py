import tkinter as tk
import random

root = tk.Tk()
root.geometry("600x600")
root.title("Let's Play to Wordle!")
root.configure(background='#58427C')

lab = tk.Label(root, text="Wordle-ENG", fg="white", font="Arial 20",
            height=1, bg="darkblue")
lab.pack(pady=20)

words_frame = tk.Frame(root)
words_frame.pack(pady=40)

def read_file(file):
    words = []
    file = open(file, "r", encoding="utf-8")
    for row in file:
        words.append(row.strip())
    return words

def choose_word(word_list):
    return random.choice(word_list)

def create_input_fields(word):
    fields = []
    for i in range(len(word)):
        input_field = tk.Entry(root, font='Arial 14', width=2, justify='center')
        input_field.grid(row=0, column=i, padx=5, pady=40)
        fields.append(input_field)
    return fields

first_row = "QWERTYUIOP"
second_row = "ASDFGHJKL"
third_row = "ZXCVBNM"
rows = [first_row, second_row, third_row]
def create_buttons():
    buttons = []
    for r in range(len(rows)):
        for index, letter in enumerate(rows[r]):
            button = tk.Button(root, text=letter, bg="gray",
            command=lambda l=letter: add_letter(l),
            width=2, font='Arial 14')
            button.grid(row=r+1, column=index)
            buttons.append(button)
    return button

def add_letter(letter):
    for input_field in fields:
        if not input_field.get():
            input_field.insert(0, letter)
            break


fields = create_input_fields(target_word, words_frame)
buttons = create_buttons(words_frame)

















def update_input_fields(fields, guess, word):
    for i, input_field in enumerate(fields):
        input_field.delete(0, tk.END)
        input_field.insert(0, guess[i].upper())
        if guess[i] == word[i]:
            input_field.config(bg='#00CC99')
        elif guess[i] in word:
            input_field.config(bg='#FFD300')
        else:
            input_field.config(bg='#536878')

def handle_guess(fields, word, attempts_label, result_label):
    guess = ''.join(input_field.get().lower() for input_field in fields)
    if len(guess) != len(word):
        result_label.config(text="Enter the word completely!")
        return
    update_input_fields(fields, guess, word)
    if guess == word:
        result_label.config(text="Congrats, you win!")
        for input_field in fields:
            input_field.config(state='disabled')
        return True
    return False

def new_game(fields, word_list, attempts_label, result_label):
    global target_word
    target_word = choose_word(word_list)
    for input_field in fields:
        input_field.config(state='normal', bg='white')
        input_field.delete(0, tk.END)
    attempts_label.config(text="Attempts: 6")
    result_label.config(text="")
    return target_word


def confirm_attempt(fields, word, attempts, attempts_label, result_label):
    if handle_guess(fields, word, attempts_label, result_label):
        return
    attempts[0] -= 1
    if attempts[0] <= 0:
        result_label.config(text=f"The game is over. The word was {word.upper()}.")
        for input_field in fields:
            input_field.config(state='disabled')
    else:
        attempts_label.config(text=f"Attempts: {attempts[0]}")


attempts = [6]
words = read_file("words.txt")
target_word = choose_word(words)

attempts_label = tk.Label(root, text=f"Attempts: {attempts[0]}", font="Arial 14")
attempts_label.pack(pady=10)

result_label = tk.Label(root, text="", font="Arial 14")
result_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=20)
input_fields = create_input_fields(len(target_word), input_frame)
for i, input_field in enumerate(input_fields):
    input_field.grid(row=0, column=i, padx=5, pady=5)

confirm_button = tk.Button(root, text="Confirm", command=lambda: confirm_attempt(input_fields, target_word, attempts, attempts_label, result_label))
confirm_button.pack(pady=20)

new_game_button = tk.Button(root, text="New game", command=lambda: new_game(input_fields, words, attempts_label, result_label))
new_game_button.pack(pady=10)

root.mainloop()