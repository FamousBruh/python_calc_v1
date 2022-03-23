from tkinter import *
import parser
from math import *
import re
from random import *

def entry_update(sv):
    text = sv.get()
    text = text.replace("^", "**")
    text = re.sub(r'([0-9]+)\(', r'\g<1>*(', text)
    ## Following code literally only exists to stop the errors from flooding console
    try:
        output_label["text"] = round(eval(text), 10)
    except:
        pass

window = Tk()

window.resizable(False, False)
window.geometry("400x300")
window.config(
    bg="#89CFF0"
    )

sv = StringVar()

sv.trace("w", lambda name, index, mode, sv=sv: entry_update(sv))

entry_box = Entry(
    window,
    bd=5,
    relief="sunken",
    width=25,
    font=("Arial", 18),
    textvariable=sv
)
entry_box.pack(ipady=2, pady=10)

output_label = Label(
    window,
    bd=2,
    relief="raised",
    justify=CENTER,
    width=25,
    font=("Arial", 16)
)
output_label.pack(pady=25)

window.mainloop()
