from tkinter import *
from math import sqrt
import NumPy as np
import matplotlib.pyplot as plt

def toSolve(event):
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    d = b**2 - 4 * a *c
    if d > 0:
        x1 = (-b + sqrt(d))/ (2 * a)
        x2 = (- b - sqrt(d))/ (2 * a)
    elif d == 0:
        x1 = (-1 * b) / (2 * a)
    else:
        x1 = Label(solution_frame,
        text = "The quadratic equation has no roots!",
        bg="yellow", font="Arial 14").pack(pady=40)


# def graf():
#     a = float(a_entry.get())
#     b = float(b_entry.get())
#     c = float(c_entry.get())

#     x0 = (-b) / 2 * a
#     y0 = a * x0 ** 2 + b * x0 + c
#     x = np.arange(x0 - 15, x0 + 15, 1)  # min, max, step
#     y = a * x ** 2 + b * x + c
#     fig = plt.figure()
#     plt.plot(x,y,'r-d')
#     plt.title("Quadratic equation")
#     plt.ylabel('Y')
#     plt.xlabel('X')
#     plt.grid(True)
#     plt.show()

root = Tk()
root.geometry("600x300")
root.title("Quadratic equation")
root.iconbitmap("q.ico")

lab = Label(root, text="Solving a quadratic equation", bg="blue",
            fg="white", font="Arial 24", height=1,)
lab.pack(fill=X)

equ_frame = Frame(root)
equ_frame.pack(pady=20)

a_entry = Entry(equ_frame, width=10, font="Arial 14")
a_entry.grid(row=0, column=0)
a_label = Label(equ_frame, text="x² + ", font="Arial 14")
a_label.grid(row=0, column=1)

b_entry = Entry(equ_frame, width=10, font="Arial 14")
b_entry.grid(row=0, column=2)
b_label = Label(equ_frame, text="x + ", font="Arial 14")
b_label.grid(row=0, column=3)

c_entry = Entry(equ_frame, width=10, font="Arial 14")
c_entry.grid(row=0, column=4)

equals_label = Label(equ_frame, text=" = 0 ", font="Arial 14")
equals_label.grid(row=0, column=5)

solve_button = Button(equ_frame, text="Solve", bg="green",
fg="white", font="Arial 14", relief=GROOVE)
solve_button.grid(row=0, column=6)

solution_frame = Frame(root, bg="yellow", height=100, width=400)
solution_frame.pack(fill=X, expand=True)

solution_label = Label(solution_frame, text="Solution", bg="yellow",
font="Arial 14")
solution_label.pack(pady=40)

    
root.mainloop()