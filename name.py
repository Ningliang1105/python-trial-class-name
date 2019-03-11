from tkinter import *

window = Tk()
window.title("输入姓名")
window.geometry('400x400')

hint = Label(window, text="请输入你的名字")
hint.pack()

name_entry = Entry(window)
name_entry.pack()

def name_break_func():
    name = name_entry.get()
    name_break.set("你姓" + name[0] + "，名" + name[1:])

outcome_button = Button(window, text="输完点我", command=name_break_func)
outcome_button.pack()

name_break = StringVar()

outcome_label = Label(window, textvariable=name_break)
outcome_label.pack()

mainloop()
