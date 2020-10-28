import json
import os
import subprocess
from tkinter import Tk, Label, Entry, StringVar, Button, ttk, messagebox

import requests



text_variable_dict = {}
url = 'http://127.0.0.1:5000/'

mygui = Tk(className='Portal Run')

mss_no = StringVar()
mss_no_label = Label(mygui, text="MSS NO", width=10).grid(row=0, column=0)
mss_no_entry = Entry(mygui, textvariable=mss_no).grid(row=0, column=1, pady=15)
mss_no.set("MSS-1001210")

def run_selenium():
    api = '/get_mss_no_details'
    myobj = {'mss_no': mss_no.get()}
    response = requests.post(url+api, data=myobj)
    if response.ok is True and response.status_code == 200:
        b = response.json()
        if os.path.exists("temp.json"):
            os.remove("temp.json")
        with open("temp.json", "w") as outfile:
            json.dump(b, outfile)
        subprocess.run(["python", "mediassist_final.py"])
    pass

loginButton = Button(mygui, text="Submit", command=run_selenium).grid(row=1, column=0)
closeButton = Button(mygui, text="Close", command=mygui.destroy).grid(row=1, column=1)


if __name__ == "__main__":
    mygui.mainloop()