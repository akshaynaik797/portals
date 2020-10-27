import json
import subprocess
from tkinter import Tk, Label, Entry, StringVar, Button, ttk, messagebox
import db_functions


text_variable_dict = {}

mygui = Tk(className='Portal data entry')

mss_no = StringVar()
mss_no_label = Label(mygui, text="MSS NO", width=10).grid(row=0, column=0)
mss_no_entry = Entry(mygui, textvariable=mss_no).grid(row=0, column=1, pady=15)
mss_no.set("0")


def save_details():
    messagebox.showinfo(message="Details saved")
    pass

def get_field_list():
    global text_variable_dict
    with open('temp.json') as fp:
        a = json.load(fp)
        values = tuple(a['Claim'][0].keys())

    insname = StringVar()
    ttk.Label(mygui, text="Insurer Name", width=10).grid(row=0, column=2, pady=15, padx=15)
    insname_entry = Entry(mygui, textvariable=insname).grid(row=0, column=3)
    insname.set("mediassist")

    process = StringVar()
    ttk.Label(mygui, text="Process", width=10).grid(row=0, column=4, pady=15, padx=15)
    process_entry = Entry(mygui, textvariable=process).grid(row=0, column=5)
    process.set("Claim")

    saveButton = Button(mygui, text="Save details", command=save_details).grid(row=1, column=1)

    result = db_functions.get_field_list(insname.get(), process.get())
    for i, j in enumerate(result):
        text_variable_dict[j] = StringVar()
        Label(mygui, text=j, width=30).grid(row=i + 2, column=0, pady=15)
        process_list = ttk.Combobox(mygui, width=25, textvariable=text_variable_dict[j])
        process_list['values'] = values
        process_list.grid(row=i + 2, column=1)
        process_list.current(0)


loginButton = Button(mygui, text="Get API & DB fields", command=get_field_list).grid(row=1, column=0)
closeButton = Button(mygui, text="Close", command=mygui.destroy).grid(row=1, column=2)


if __name__ == "__main__":
    mygui.mainloop()