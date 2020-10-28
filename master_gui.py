import json
import subprocess
from tkinter import Tk, Label, Entry, StringVar, Button, ttk, messagebox

import requests

import db_functions

text_variable_dict, temp_json = {}, {}

mygui = Tk(className='Portal data entry')

mss_no = StringVar()
mss_no_label = Label(mygui, text="MSS NO", width=10).grid(row=0, column=0)
mss_no_entry = Entry(mygui, textvariable=mss_no).grid(row=0, column=1, pady=15)
# mss_no.set("MSS-1001210")

insname = StringVar()
ttk.Label(mygui, text="Insurer Name", width=10).grid(row=0, column=2, pady=15, padx=15)
insname_entry = Entry(mygui, textvariable=insname).grid(row=0, column=3)
insname.set('')

process = StringVar()
ttk.Label(mygui, text="Process", width=10).grid(row=0, column=4, pady=15, padx=15)
process_list = ttk.Combobox(mygui, width=12, textvariable=process)
# process_list['values'] = ('msg', 'preauth', '0', 'Enhancement', 'Query Replied', 'Claim')
process_list.grid(row=0, column=5)


def get_ins_process():
    global temp_json
    url = 'https://vnusoftware.com/iclaimmax/api/preauth/'
    myobj = {'pid': mss_no.get()}
    response = requests.post(url, data=myobj)
    if response.ok is True and response.status_code == 200:
        temp_json = b = response.json()
        process = tuple(b.keys())
        insname.set(b['0']['insname'])
        process_list['values'] = process


def save_details():
    global text_variable_dict
    map_dict = {i: text_variable_dict[i].get() for i in text_variable_dict}
    data_dict = {i: temp_json[process.get()][0][text_variable_dict[i].get()] for i in map_dict}
    data_dict['process'] = process.get()
    data_dict['insname'] = insname.get()
    data_dict['login_details'] = db_functions.get_portal_details_dict(insname.get(), process.get())
    data_dict['claimno'] = temp_json['0']['ClaimId']
    data_dict['mss_no'] = mss_no.get()
    data = json.dumps(data_dict)
    db_functions.save_mss_no_data(mss_no.get(), data)
    messagebox.showinfo(message="Details saved")
    pass

def get_field_list():
    global text_variable_dict
    with open('temp.json') as fp:
        a = json.load(fp)
        values = tuple(a['Claim'][0].keys())

    # saveButton = Button(mygui, text="Save details", command=save_details).grid(row=1, column=2)

    result = db_functions.get_field_list(insname.get(), process.get())
    for i, j in enumerate(result):
        saveButton = Button(mygui, text="Save details", command=save_details).grid(row=1, column=2)
        text_variable_dict[j] = StringVar()
        Label(mygui, text=j, width=30).grid(row=i + 2, column=0, pady=15)
        process_list = ttk.Combobox(mygui, width=25, textvariable=text_variable_dict[j])
        process_list['values'] = values
        process_list.grid(row=i + 2, column=1)
        process_list.current(0)

ins_process_Button = Button(mygui, text="Get Insurer and Process", command=get_ins_process).grid(row=1, column=0)
loginButton = Button(mygui, text="Get API & DB fields", command=get_field_list).grid(row=1, column=1)
closeButton = Button(mygui, text="Close", command=mygui.destroy).grid(row=1, column=3)


if __name__ == "__main__":
    mygui.mainloop()