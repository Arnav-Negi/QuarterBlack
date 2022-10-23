from tkinter import *
import tkinter.font as tkfont
from insert_seat_preference import insert_seat_preference
from userlogin import check_record
from userregistration import add_record

email_loggged_in = "NA"
logged_in = 0
interface = Tk()
#interface.configure(background="gray")
interface.title('Login Page')
interface.state('zoomed')
interface.resizable(width = False, height = False)

interface.grid_columnconfigure(0, weight = 1)
interface.grid_rowconfigure(0, weight = 1)

'''Submit button for login page'''
def submit_login(email, pwd, frame: Frame) :
    global email_loggged_in, logged_in, Valid
    res = check_record(email, pwd)
    if res == -1 :
        Valid.configure(text="Username or Password does not exist")
        return

    frame.grid_forget()
    frame_submit = Frame(interface)    
    frame_submit.grid(row=0, column=0)

    lbl = Label(frame_submit)
    lbl.grid(row=0, column=0)
    email_loggged_in = email
    logged_in = 1
    # lbl.configure(text="Welcome " + email)
    # lbl['font'] = tkfont.Font(family = 'Jokerman', size=45, weight = 'bold')
    main_page()

'''Displays login form. Queries DB to check for valid login.'''
def login_page(frame_main: Frame) :
    global interface, Valid
    
    frame_main.destroy()
    frame_login = Frame(interface, width=50, height=25)
    frame_login.grid(row=0, column=0)

    heading = Label(frame_login, text="Login Page", fg="black")
    heading['font'] = tkfont.Font(family="Monospace", size=70, weight="bold")
    heading.grid(row=0, column=0, columnspan=2)
    #heading.grid(row=2, column=0)  

    Label(frame_login).grid(row=1,column = 0)
    Label(frame_login).grid(row=2,column = 0)
    Label(frame_login).grid(row=3,column = 0)

    email_login = Label(frame_login, text="Email")
    email_login.grid(row=4, column=0)
    email_login['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')
    Label(frame_login).grid(row=5,column = 0)
    pwd_login = Label(frame_login, text="Password")
    pwd_login.grid(row=6, column=0)
    pwd_login['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')

    email_entry = Entry(frame_login)
    email_entry.grid(row=4, column=1)
    email_entry['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')
    pwd_entry = Entry(frame_login)
    pwd_entry.grid(row=6, column=1)
    pwd_entry['font'] = tkfont.Font(family = 'Arial', size=20, weight = 'bold')

    Label(frame_login).grid(row=7,column = 0)
    Label(frame_login).grid(row=8,column = 0)
    Label(frame_login).grid(row=10,column = 0)
    Valid = Label(frame_login, fg = 'red')
    Valid.grid(row=11,column = 0, columnspan=2)
    Valid['font'] = tkfont.Font(family = 'Arial', size=10, weight = 'bold', slant='italic')

    Submit = Button(frame_login, text = 'Submit', fg = '#FF7000', \
        command=lambda: submit_login(email_entry.get(), pwd_entry.get(), frame_login))
    Submit.grid(row=9, column=0, columnspan=2)
    Submit['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')

def submit_add_user(email, pwd, frame: Frame) :
    res = add_record(email, pwd)
    if res == -1 :
        # email already exists.
        warning = Label(frame, text="Account with given email already.")
        Label.grid(row=3, column=0)
    else :
        warning = Label(frame, text="Account added.")
        warning.grid(row=3, column=0)

def add_user(frame_main) :
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
        command=lambda: submit_add_user(email_entry.get(), pwd_entry.get(), frame_login))
    Submit.grid(row=5, column=0)
    Submit['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')


def submit_update(angle, x, y, frame_update: Frame):
    insert_seat_preference(email_loggged_in, angle, x, y)
    frame_update.grid_forget()
    main_page()

def update_settings(frame_main: Frame):
    global interface

    frame_main.destroy()
    frame_update = Frame(interface)
    frame_update.grid(row=0, column=0)

    heading = Label(frame_update, text="Login Page", fg="black")
    heading['font'] = tkfont.Font(family="Monospace", size=70, weight="bold")
    heading.grid(row=1, column=0, columnspan=2)
    #heading.grid(row=2, column=0)

    angle_lbl = Label(frame_update, text="Angle")
    angle_lbl.grid(row=2, column=0)
    angle_lbl['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')
    x_lbl = Label(frame_update, text="x")
    x_lbl.grid(row=3, column=0)
    x_lbl['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')
    y_lbl = Label(frame_update, text="y")
    y_lbl.grid(row=4, column=0)
    y_lbl['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')

    angle_entry = Entry(frame_update)
    angle_entry.grid(row=2, column=1)
    angle_entry['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')
    x_entry = Entry(frame_update)
    x_entry.grid(row=3, column=1)
    x_entry['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')
    y_entry = Entry(frame_update)
    y_entry.grid(row=4, column=1)
    y_entry['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')

    Submit = Button(frame_update, text = 'Submit', fg = '#FF7000', \
        command=lambda: submit_update(angle_entry.get() ,x_entry.get(), y_entry.get(), frame_update))
    Submit.grid(row=5, column=0, columnspan=2)
    Submit['font'] = tkfont.Font(family = 'Jokerman', size=20, weight = 'bold')

def main_page() :
    global logged_in, email_loggged_in
    frame_main = Frame(interface, width=50, height=25)
    frame_main.grid(row=0,column=0)

    if logged_in == 0:
        heading = Label(frame_main,text = 'Login Page', fg = 'red')
        heading['font'] = tkfont.Font(family = 'Jokerman', size=70, weight = 'bold')
        heading.grid(row = 0,column = 0)

        Label(frame_main).grid(row=1,column = 0)
        Label(frame_main).grid(row=2,column = 0)

        Login_btn = Button(frame_main, text = 'Login', fg = '#FF7000', command=lambda: login_page(frame_main))
        Login_btn['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        Login_btn.grid(row = 3, column = 0)

        Label(frame_main).grid(row=4,column = 0)
        Label(frame_main).grid(row=5,column = 0)

        New = Button(frame_main, text = 'New User', fg = '#FF7000', command=lambda: add_user(frame_main))
        New['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        New.grid(row = 6, column = 0)

    else:
        heading = Label(frame_main,text = 'Welcome ' + email_loggged_in, fg = 'red')
        heading['font'] = tkfont.Font(family = 'Jokerman', size=70, weight = 'bold')
        heading.grid(row = 0,column = 0)

        Label(frame_main).grid(row=1,column = 0)
        Label(frame_main).grid(row=2,column = 0)

        Login = Button(frame_main, text = 'Change User', fg = '#FF7000', command=lambda: login_page(frame_main))
        Login['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        Login.grid(row = 3, column = 0)

        Label(frame_main).grid(row=4,column = 0)
        Label(frame_main).grid(row=5,column = 0)

        New = Button(frame_main, text = 'New User', fg = '#FF7000', command=lambda: add_user(frame_main))
        New['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        New.grid(row = 6, column = 0)

        Label(frame_main).grid(row=7,column = 0)
        Label(frame_main).grid(row=8,column = 0)

        New = Button(frame_main, text = 'Update settings', fg = '#FF7000', command=lambda: update_settings(frame_main))
        New['font'] = tkfont.Font(family = 'Verdana', size=45, weight = 'bold')
        New.grid(row = 9, column = 0)

main_page()
interface.mainloop()