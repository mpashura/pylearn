import random
from tkinter import *
import tkinter
# int age = 5
# age = 0

# if age < 500 and age > 30:
#    print('f')

a = [7, 8, 3, 6, 1, 0, 9, 5, 4, 2]
a.sort()
print(a)


def a_action():
    print("Pressed A")


def b_action():
    print("Pressed B")

window = Tk()

buttonA = Button(window, text='press me', command=a_action)
buttonB = Button(window, text='don\'t press', command=b_action)
buttonA.pack()
buttonB.pack()

# window.test()


window.mainloop()
