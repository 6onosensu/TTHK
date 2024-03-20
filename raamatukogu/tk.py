from tkinter import *
from functions import *

root = Tk()
root.geometry("600x600")
root.title("Library")
root.configure(background='#290700')

welcomeFrame = Frame(root, bg='#290700')
welcomeFrame.pack(pady=20)

welcomeLab = Label(welcomeFrame, text="Welcome! What cat I help you find?", fg="#FFFFFF", font="Arial 20",
            height=1, bg='#290700')
welcomeLab.pack(pady=20)

searchEntry = Entry(welcomeFrame, font='Arial 20', bg="#E8D8D6", fg="#290700", )
searchEntry.pack(pady=10)
searchEntry.bind('<Return>', searching)

root.mainloop()
