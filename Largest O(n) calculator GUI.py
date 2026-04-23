from tkinter import *
from main import *

root = Tk()
root.title("O(f(n)) = x")
labelx = Label(root, text="x: ")
entryx = Entry(root)
labelx.grid(row=0, column=0)
entryx.grid(row=0, column=1, columnspan=2, pady=2)

labeln = Label(root, text="n: ")
resultn = Label(root, text = "", bd=2, relief="ridge", width=17)
labeln.grid(row=1, column=0)
resultn.grid(row=1, column=1, columnspan=2, pady=10)

def click_a():
    arg = eval(entryx.get())
    ans = logarithmic(arg)
    resultn.config(text = ans)

def click_b():
    arg = eval(entryx.get())
    ans = square_root(arg)
    resultn.config(text = ans)

def click_c():
    arg = eval(entryx.get())
    ans = linear(arg)
    resultn.config(text = ans)

def click_d():
    arg = eval(entryx.get())
    ans = log_linear(arg)
    resultn.config(text = ans)

def click_e():
    arg = eval(entryx.get())
    ans = quadratic(arg)
    resultn.config(text = ans)

def click_f():
    arg = eval(entryx.get())
    ans = cubic(arg)
    resultn.config(text = ans)

def click_g():
    arg = simple_eval(entryx.get())
    ans = exponential(arg)
    resultn.config(text = ans)

def click_h():
    arg = eval(entryx.get())
    ans = factorial(arg)
    resultn.config(text = ans)

def click_clr():
    resultn.config(text = "")
    entryx.delete(0, END)


a = Button(root, text="logn ", padx=10, pady=10, width=5, command=click_a)
b = Button(root, text="√n", padx=10, pady=10, width=5, command=click_b)
c = Button(root, text="n", padx=10, pady=10, width=5, command=click_c)

d = Button(root, text="nlogn", padx=10, pady=10, width=5, command=click_d)
e = Button(root, text="n2", padx=10, pady=10, width=5, command=click_e)
f = Button(root, text="n3", padx=10, pady=10, width=5, command=click_f)

g = Button(root, text=" 2n ", padx=10, pady=10, width=5, command=click_g)
h = Button(root, text="n!", padx=10, pady=10, width=5, command=click_h)
clr = Button(root, text="clr", padx=10, pady=10, width=5, command=click_clr)

a.grid(row=2, column=0)
b.grid(row=2, column=1)
c.grid(row=2, column=2)

d.grid(row=3, column=0)
e.grid(row=3, column=1)
f.grid(row=3, column=2)

g.grid(row=4, column=0)
h.grid(row=4, column=1)
clr.grid(row=4, column=2)

root.mainloop()