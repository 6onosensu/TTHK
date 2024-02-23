from tkinter import *
from game import *

class WordleApp:
    def __init__(self, root):
        self.root = root
        self.game = Game()
        self.create_window()

    def create_window(self):
        s

root = Tk()
root.geometry("600x600")
root.title("Let's Play to Wordle!")
root.iconbitmap("")
root.configure(background='darkblue')

lab = Label(root, text="Wordle-ENG", fg="white", font="Arial 20",
            height=1, bg="darkblue").pack(pady=20)

worldsFrame = Frame(root).pack(pady=40)


if __name__ == "__main__":
    root = Tk()
    root.title("Wordle Game")
    app = WordleApp(root)
    root.mainloop()


