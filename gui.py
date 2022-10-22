from distutils.log import Log
from tkinter import *
import tkinter.font as tkfont

from pyparsing import col

from userlogin import check_record

interface = Tk()
interface.configure(background="gray")
interface.title('Login Page')
interface.state('normal')
interface.resizable(width = False, height = False)

interface.grid_columnconfigure(0, weight = 1)
interface.grid_rowconfigure(0, weight = 1)

'''Submit button for login page'''
def submit_login(email, pwd, frame: Frame) :
    frame.grid_forget()
    frame_submit = Frame(interface)
    res = check_record(email, pwd)
    frame_submit.grid(row=0, column=0)

    lbl = Label(frame_submit)
    lbl.grid(row=0, column=0)
    if res == -1 :
        lbl.configure(text="User not found.")
        lbl['font'] = tkfont.Font(family = 'Jokerman', size=45, weight = 'bold')
    else :
        lbl.configure(text="Welcome User")
        lbl['font'] = tkfont.Font(family = 'Jokerman', size=45, weight = 'bold')

'''Displays login form. Queries DB to check for valid login.'''
def Login() :
    global interface

    frame_main.destroy()
    frame_login = Frame(interface, width=50, height=25)
    frame_login.grid(row=0, column=0)

    heading = Label(frame_login, text="Login Page", fg="black")
    heading['font'] = tkfont.Font(family="Monospace", size=70, weight="bold")
    heading.grid(row=1, column=0)
    heading.grid(row=2, column=0)

    email_login = Label(frame_login, text="Email")
    email_login.grid(row=3, column=0)
    email_login['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')
    pwd_login = Label(frame_login, text="Password")
    pwd_login.grid(row=4, column=0)
    pwd_login['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')

    email_entry = Entry(frame_login)
    email_entry.grid(row=3, column=1)
    email_entry['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')
    pwd_entry = Entry(frame_login)
    pwd_entry.grid(row=4, column=1)
    pwd_entry['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')

    Submit = Button(frame_login, text = 'Submit', fg = '#FF7000', \
        command=lambda: submit_login(email_entry.get(), pwd_entry.get(), frame_login))
    Submit.grid(row=5, column=0)
    Submit['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')



frame_main = Frame(interface, width=50, height=25)
frame_main.grid(row=0,column=0)

heading = Label(frame_main,text = 'Login Page', fg = 'red')
heading['font'] = tkfont.Font(family = 'Jokerman', size=70, weight = 'bold')
heading.grid(row = 0,column = 0)

Label(frame_main).grid(row=1,column = 0)
Label(frame_main).grid(row=2,column = 0)

Login = Button(frame_main, text = 'Login', fg = '#FF7000', command=Login)
Login['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
Login.grid(row = 3, column = 0)

Label(frame_main).grid(row=4,column = 0)
Label(frame_main).grid(row=5,column = 0)

New = Button(frame_main, text = 'New User', fg = '#FF7000')
New['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
New.grid(row = 6, column = 0)

interface.mainloop()