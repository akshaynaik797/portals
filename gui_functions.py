from tkinter import Tk, Label, Entry, StringVar, Button, ttk, messagebox
from PIL import Image, ImageTk

cap_gui = Tk(className='Enter Captcha')
cap_gui.geometry("500x200")

def get_captcha_no():
    a = captcha_no.get()
    if a is '':
        messagebox.showerror("Error", "Enter capcha")
    else:
        cap_gui.destroy()
        return a

captcha_no = StringVar()
captcha_no_label = Label(cap_gui, text="Enter Capcha", width=10).grid(row=0, column=0)
captcha_no_entry = Entry(cap_gui, textvariable=captcha_no).grid(row=0, column=1, pady=15)

def wait_popup():
    root = Tk()
    root.withdraw()
    try:
        cap_gui.withdraw()
    except:
        pass
    state = messagebox.askokcancel("Confirm", "Do you want to wait?")
    root.update()
    return state


def capcha_popup():
    try:
        img = ImageTk.PhotoImage(Image.open('capcha.jpeg'))
    except FileNotFoundError:
        messagebox.showerror("Error", "Capcha image not found")
        exit()

    panel = Label(cap_gui, image=img).grid(row=0, column=2, pady=15)
    captcha_no_button = Button(cap_gui, text="OK", command=get_captcha_no).grid(row=1, column=0)

    cap_gui.mainloop()
    return captcha_no.get()


if __name__ == "__main__":
    cap_gui.mainloop()
