from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

current_input = StringVar()
display = ttk.Label(frm, textvariable=current_input)
display.grid(row=0, column=0, columnspan=3)

def calculate():
    try:
        result = eval(current_input.get())
        current_input.set(str(result))
    except:
        current_input.set("error")
def add_digit(digit):
    current = current_input.get()
    current_input.set(current + str(digit))

def clear():
    current_input.set("")

for i in range(3):
    for j in range(3):
        num = i*3 + j + 1
        ttk.Button(frm, text=str(num), command=lambda x=num: add_digit(x)).grid(row=i+1, column=j)

ops =['+', '-', '/', '*','Sof']
for i, op in enumerate(ops):
    ttk.Button(frm,text=op, command= lambda x=op: add_digit(x)).grid(row=i+1, column = 4)

ttk.Button(frm, text="Clear", command=clear).grid(row=5, column=0)
ttk.Button(frm, text="0", command=lambda x= 0: add_digit(x)).grid(row=4, column=1)

ttk.Button(frm, text='=', command= calculate).grid(row=10, column=1, columnspan=2)


root.mainloop()