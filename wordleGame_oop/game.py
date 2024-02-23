import random

class Game:
    def __init__(self):
        self.readed: list = self.read_file("words.txt")
        self.target_w = self.select_word()
        self.attempts = 0
        self.max_attempts = 6
        self.history = []
    


