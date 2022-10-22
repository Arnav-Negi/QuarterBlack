from tkinter import *
import tkinter.font as tkfont

interface = Tk()
interface.title('Login Page')
interface.state('zoomed')
interface.resizable(width = False, height = False)

interface.grid_columnconfigure(0, weight = 1)
interface.grid_rowconfigure(0, weight = 1)

frame1 = Frame(interface)
frame1.grid(row=0,column=0)

heading = Label(frame1,text = 'Login Page', fg = 'red')
heading['font'] = tkfont.Font(family = 'Jokerman', size=70, weight = 'bold')
heading.grid(row = 0,column = 0)

Label(frame1).grid(row=1,column = 0)
Label(frame1).grid(row=2,column = 0)

Login = Button(frame1, text = 'Old User', fg = '#FF7000')
Login['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
Login.grid(row = 3, column = 0)

Label(frame1).grid(row=4,column = 0)
Label(frame1).grid(row=5,column = 0)

New = Button(frame1, text = 'New User', fg = '#FF7000')
New['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
New.grid(row = 6, column = 0)

interface.mainloop()