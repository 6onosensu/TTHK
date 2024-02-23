from tkinter import *

class WordleBoard(Frame):
    def __init__(self, master, game_instance, **kwargs):
        super().__init__(master, **kwargs)
        self.game = game_instance
        self.create_board()

    def create_board(self):
        self.letter_labels = []
        for i in range(self.game.max_attempts):
            row = []
            for j in range(len(self.game.target_word)):
                label = Entry(self, text="", borderwidth=2,
                              relief="groove", width=3, height=1)
                label.grid(row=i, column=j, padx=5, pady=5)
                row.append(label)
            self.letter_labels.append(row)

    def update_board(self):
        for i, guess in enumerate(self.game.history):
            for j, char in enumerate(guess):
                self.letter_labels[i][j]['text'] = char
                if self.game.check_char_position(char, j):
                    self.letter_labels[i][j]['bg'] = 'green'
                elif self.game.check_char_presence(char):
                    self.letter_labels[i][j]['bg'] = 'yellow'
                else:
                    self.letter_labels[i][j]['bg'] = 'grey'

