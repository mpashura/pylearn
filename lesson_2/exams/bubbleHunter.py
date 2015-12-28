from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

score = 0
#  Drawing the window
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title("Bubble Hunter Game")

c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()

#  Drawing the ship
ship_id1 = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SHIP_R = 15
MIX_X = WIDTH / 2
MIX_Y = HEIGHT / 2
c.move(ship_id1, MIX_X, MIX_Y)
c.move(ship_id2, MIX_X, MIX_Y)

SHIP_SPD = 10


#  Moving ship
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id1, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id1, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship_id1, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
    elif event.keysym == 'Right':
        c.move(ship_id1, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)

c.bind_all('<Key>', move_ship)


# Drawing the bubbles
bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100


def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))


def move_bubble():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)

BUB_CHANGE = 10


#  Coordinates
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[2])/2
    return x, y


#  Deleting
def del_bubbles(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]


def clean_bubbles():
    for i in range(len(bub_id) - 1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubbles(i)


def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2-x1)**2 + (y2-y1)**2)


def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubbles(bub)
    return points


#  Main Game loop
while True:
    if randint(1, BUB_CHANGE) == 1:
        create_bubble()
    move_bubble()
    clean_bubbles()
    score += collision()
    print(score)
    window.update()
    sleep(0.01)


mainloop()
