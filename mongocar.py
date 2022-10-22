import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

window = tk.Tk()

greeting = tk.Label(text="This is in window",
height= ,fg="black", bg="white")
greeting['font'] = tkfont.Font(family='Monospace', size=25)
greeting.pack()

login_button = tk.Button(text="LOGIN", bg="white")
login_button.pack()
window.mainloop()
