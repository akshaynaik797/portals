import json
import subprocess
from tkinter import Tk, Label, Entry, StringVar, Button, ttk, messagebox
import db_functions


text_variable_dict = {}

mygui = Tk(className='Portal Run')

mss_no = StringVar()
mss_no_label = Label(mygui, text="MSS NO", width=10).grid(row=0, column=0)
mss_no_entry = Entry(mygui, textvariable=mss_no).grid(row=0, column=1, pady=15)
mss_no.set("0")

def run_selenium():
    subprocess.run(["python", "mediassist.py"])
    pass

loginButton = Button(mygui, text="Submit", command=run_selenium).grid(row=1, column=0)
closeButton = Button(mygui, text="Close", command=mygui.destroy).grid(row=1, column=1)


if __name__ == "__main__":
    mygui.mainloop()