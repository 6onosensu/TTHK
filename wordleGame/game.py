from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Let's Play to Wordle!")
root.iconbitmap("")
root.configure(background='darkblue')

lab = Label(root, text="Wordle-ENG", fg="white", font="Arial 20",
            height=1, bg="darkblue").pack(pady=20)

worldsFrame = Frame(root).pack(pady=40)


root.mainloop()