from random import randint
# from tkinter.colorchooser import *
from tkinter import *


def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(1,6)))

window = Tk()

# window = askcolor()

text = Text(window, width=2, height=2)
buttonA = Button(window, text='press to roll', command=roll)
text.pack()
buttonA.pack()

window.mainloop()
