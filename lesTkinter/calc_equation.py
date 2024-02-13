from tkinter import *


root = Tk()
root.geometry("600x300")
root.title("Quadratic equation")
root.iconbitmap("q.ico")

lab = Label(root, text="Solving a quadratic equation", bg="blue",
            fg="white", font="Arial 24", height=1,)
lab.pack(fill=X)

equ_frame = Frame(root)
equ_frame.pack(pady=20)

a_entry = Entry(equ_frame, width=10)
a_entry.grid(row=0, column=0)
a_label = Label(equ_frame, text="x² + ")
a_label.grid(row=0, column=1)

b_entry = Entry(equ_frame, width=10)
b_entry.grid(row=0, column=2)
b_label = Label(equ_frame, text="x + ")
b_label.grid(row=0, column=3)

c_entry = Entry(equ_frame, width=10)
c_entry.grid(row=0, column=4)

equals_label = Label(equ_frame, text=" = 0")
equals_label.grid(row=0, column=5)

solve_button = Button(equ_frame, text="Solve", bg="green", fg="white")
solve_button.grid(row=0, column=6)

solution_frame = Frame(root, bg="yellow", height=100, width=400)
solution_frame.pack(fill=X, expand=True)

solution_label = Label(solution_frame, text="Solution", bg="yellow")
solution_label.pack(pady=40)

    
root.mainloop()