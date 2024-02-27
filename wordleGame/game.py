from tkinter import *
import random

def txt_to_list(file):
    words = []
    file = open(file, "r", encoding="utf-8")
    for row in file:
        words.append(row.strip())
    return words

def get_random_word(words):
    word = random.choice(words).upper()
    return len(word), word

def max_attempts(len):
    if len > 5:
        max = 7
    else:
        max = 6
    return max

def create_entries(w, ent_f, max, vcmd):
    entries = [[] for _ in range(max)]
    for a in range(max):
        for i in range(w):
            entry_text = StringVar(ent_f)  # Creates a StringVar object to track changes in the entry
            entry = Entry(ent_f, font='Arial 14', width=2, 
                          bg="#FFFFFF", justify='center',
                          disabledbackground="#9EB9D4",
                          textvariable=entry_text,  # Associates a StringVar to the entry to track its content
                          validate="key", validatecommand=vcmd)  # vcmd - validate command
            entry.grid(row=a, column=i, padx=5, pady=5)
            # Sets a trace callback on the StringVar to limit the entry size
            entry_text.trace('w', lambda *args, e=entry,
                             var=entry_text: limit_entry_size(e, var))
            entries[a].append(entry)
            entry.bind('<Return>', on_enter_pressed)  # Binds the Enter key to the on_enter_pressed function
            if i > 0:
                entries[a][i-1].next_entry = entry  # attribute is adding to each 'Entry' widget to keep track of the next one
        if a > 0:
            for field in fields[a]:
                field.config(state='disabled')
    return entries

def on_enter_pressed(event):
    confirm()

def limit_entry_size(entry, var):
    value = var.get()
    if len(value) > 1:
        var.set(value[:1])  # Method of the class StringVar, '.set' cuts the string to the desired character
    if len(value) == 1:
        try:
            entry.next_entry.focus_set()  # Method of the widget "Entry", '.focus_set' for moving the input focus
        except AttributeError:  # 'list' object has no attribute 'delete'
            pass

def create_keyboard_buttons(rows, btns, cmnd):
    buttons = {}
    for _, row in enumerate(rows):
        row_frame = Frame(root, bg='#2E5894')
        row_frame.pack(side=TOP, pady=2)
        for letter in row:
            button = Button(row_frame, text=letter, width=2,
                            command=lambda l=letter: add_letter(l),
                            font='Arial 14', bg="#BCD4E6")
            button.pack(side=LEFT, padx=2)
            buttons[letter] = button
    kb_frame = Frame(root, bg='#2E5894')
    kb_frame.pack(side=TOP, pady=2)
    for i in range(3):
        btn = Button(kb_frame, text=btns[i], command=cmnd[i],
                     width=10, font='Arial 14', bg="#BCD4E6")
        btn.pack(side=RIGHT, padx=2)
    return buttons

def only_letters(input):
    if input.isalpha() or input == "":
        return True
    else:
        return False

def add_letter(letter):
    global attempt, fields
    for field in fields[attempt]:
        if not field.get():  # if not empty
            field.insert(END, letter.upper())
            break

def erase():
    global attempt, fields
    for entry in fields[attempt]:
        entry.delete(0, END)

def confirm():
    global attempt, fields, word
    current_entries = fields[attempt]
    guess = ''.join(entry.get() for entry in current_entries).upper()
    if len(guess) != word_len:
        return
    update_colors(current_entries, guess, word)
    is_win = guess == word
    if is_win or attempt == max - 1:
        end_game(is_win, word)
    else:
        attempt += 1
        if attempt < max:
            for field in fields[attempt]:
                field.config(state='normal')

def new_game():
    global attempt, word, word_len, fields, ent_f, vcmd
    attempt = 0
    word_len, word = get_random_word(words)
    max = max_attempts(word_len)
    for row in fields:
        for entry in row:
            entry.destroy()
    fields = create_entries(word_len, ent_f, max, vcmd)
    result_label.config(text="")

def end_game(win, word):
    if win:
        rText = f"Congratulations! You guessed the word '{word}' in {attempt + 1} tries."
    else: 
        rText = f"The game is over. The word was: {word}."
    result_label.config(text=rText)
    for attempt_fields in fields:
        for field in attempt_fields:
            field.config(state='disabled')

def update_colors(fields, guess, word):
    for i, field in enumerate(fields):
        guessed_letter = guess[i]
        letter = word[i]
        if letter == guessed_letter:
            field.config(bg = "#3B7A57", disabledbackground="#5F9EA0")
        elif guessed_letter in word:
            field.config(bg = "#FFBF00", disabledbackground="#feffd4")
        else:
            field.config(bg = "#BCD4E6", disabledbackground="#9EB9D4")

root = Tk()
root.geometry("600x600")
root.title("Let's Play to Wordle!")
root.iconbitmap("word.ico")
root.configure(background='#2E5894')

lab = Label(root, text="Wordle-ENG", fg="#FAEBD7", font="Arial 20",
            height=1, bg="#2E5894")
lab.pack(pady=20)

ent_f = Frame(root, bg='#2E5894')
ent_f.pack(pady=20)

first_row = "QWERTYUIOP"
second_row = "ASDFGHJKL"
third_row = "ZXCVBNM"
rows = [first_row, second_row, third_row]
btns = ['New Game!', 'Confirm', 'Erase']
cmnds = [new_game, confirm, erase]
attempt = 0

words = txt_to_list("words.txt")
word_len, word = get_random_word(words)
max = max_attempts(word_len)
# %P- is a special validation var in Tkinter, the value that will be entered into the widget if the validation succeeds
vcmd = (root.register(only_letters), '%P')
fields = create_entries(word_len, ent_f, max, vcmd)
buttons = create_keyboard_buttons(rows, btns, cmnds)

result_label = Label(root, text="",  fg="#FAEBD7",
                     font = "Arial 14", bg='#2E5894')
result_label.pack(pady=20)

root.mainloop()


