from tkinter import *

def toLable(event):
    t = ent.get()
    l.configure(text = t)

def choose():
    t = var.get()
    ent.delete(0, END)
    ent.insert(END, t)

def show_s(event):
    ent.configure(show="*")

window = Tk()
window.geometry("600x500")
window.title("Book")
window.iconbitmap("icon.ico")

f = Frame(window, bg="#1B2C41", border=10, height=100, width=600)

l = Label(f, text="Captition", bg="#2C4A70", fg="white", font="Arial 24",
         height=3, width=16)

ent = Entry(f, fg="gold", bg="#2C4A70", width=16, font="Arial 18",
           justify=CENTER) # show = "*"

btn = Button(f, text="Read!", font="Arial 18", fg="#1B2C41", bg="lightblue",
            relief=RAISED)  # GROOVE, SUNKEN


var = IntVar()  # StringVar()

rb1 = Radiobutton(f, text="First", font="Algerian 14", variable=var, value=1, command=choose)
rb2 = Radiobutton(f,text="Second", font="Algerian 14", variable=var, value=2, command=choose)
rb3 = Radiobutton(f,text="Third", font="Algerian 14", variable=var, value=3, command=choose)



btn.bind("<Button-1>", toLable)  # LKM
ent.bind("<Return>", show_s)  # Enter

objects = [l, ent, btn, rb1, rb2, rb3]
for i in range(len(objects)):
    objects[i].pack()
f.grid(row=0, column=0)  # pack(), place()

# l.pack()
# ent.pack()
# btn.pack()

window.mainloop()