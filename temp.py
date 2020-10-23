from time import sleep
from tkinter import messagebox

while 1:
    state = messagebox.askquestion("Confirm","Do you want to wait??")
    if state == 'yes':
        print('waiting')
        sleep(2)
        continue
    else:
        break
