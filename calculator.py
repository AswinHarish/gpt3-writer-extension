from tkinter import *

window = Tk()
window.title("Calculator - By Aswin")
window.configure(bg="black")
window.iconbitmap('calculator.ico')

e = Entry(window, width=10, borderwidth=5, font=('Helvetica', 44))
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


#  define buttons
button_1 = Button(window, text="1", padx=30, pady=20, borderwidth=5, command=lambda: button_click(1),
                  activebackground="grey")
button_2 = Button(window, text="2", padx=30, pady=20, borderwidth=5, command=lambda: button_click(2),
                  activebackground="grey")
button_3 = Button(window, text="3", padx=30, pady=20, borderwidth=5, command=lambda: button_click(3),
                  activebackground="grey")
button_4 = Button(window, text="4", padx=30, pady=20, borderwidth=5, command=lambda: button_click(4),
                  activebackground="grey")
button_5 = Button(window, text="5", padx=30, pady=20, borderwidth=5, command=lambda: button_click(5),
                  activebackground="grey")
button_6 = Button(window, text="6", padx=30, pady=20, borderwidth=5, command=lambda: button_click(6),
                  activebackground="grey")
button_7 = Button(window, text="7", padx=30, pady=20, borderwidth=5, command=lambda: button_click(7),
                  activebackground="grey")
button_8 = Button(window, text="8", padx=30, pady=20, borderwidth=5, command=lambda: button_click(8),
                  activebackground="grey")
button_9 = Button(window, text="9", padx=30, pady=20, borderwidth=5, command=lambda: button_click(9),
                  activebackground="grey")
button_0 = Button(window, text="0", padx=30, pady=20, borderwidth=5, command=lambda: button_click(0),
                  activebackground="grey")
button_p = Button(window, text="AC", padx=25, pady=20, borderwidth=5, command=lambda: button_clear(),
                  activebackground="grey")
button_d = Button(window, text="/", padx=31, pady=20, borderwidth=5, command=lambda: button_divide(), bg="orange",
                  activebackground="grey")
button_e = Button(window, text="=", padx=28, pady=20, borderwidth=5, command=button_equal, bg="orange",
                  activebackground="grey")
button_a = Button(window, text="+", padx=28, pady=20, borderwidth=5, command=button_add, bg="orange",
                  activebackground="grey")
button_s = Button(window, text="-", padx=31, pady=20, borderwidth=5, command=lambda: button_subtract(), bg="orange",
                  activebackground="grey")
button_m = Button(window, text="x", padx=30, pady=20, borderwidth=5, command=lambda: button_multiply(), bg="orange",
                  activebackground="grey")

#  put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_a.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_s.grid(row=2, column=3, pady=2)

button_7.grid(row=1, column=0, padx=5)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_m.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_p.grid(row=4, column=1)
button_d.grid(row=4, column=2, padx=5, pady=2)
button_e.grid(row=4, column=3)

window.mainloop()
