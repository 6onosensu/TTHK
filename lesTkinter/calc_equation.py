from tkinter import *


calc_window = Tk()
calc_window.geometry("600x200")
calc_window.title("Quadratic equation")
calc_window.iconbitmap("calculator.ico")



lab = Label(text="Solving a quadratic equation", bg="#1b6478", fg="white", font="Arial 24",
            height=1,)

row = []
ent_a = Entry(row, bg="#1b6478", fg="white", font="Arial 18")
ent_b = Entry(row, bg="#1b6478", fg="white", font="Arial 18")
ent_c = Entry(row, bg="#1b6478", fg="white", font="Arial 18")


objects = [lab, row]

for i in range(len(objects)):
    objects[i].pack()

row = [ent_a, ent_b, ent_c]
for element in range(len(row)):
    row[element].grid()
    
calc_window.mainloop()