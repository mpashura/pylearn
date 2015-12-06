import turtle as star
from time import sleep

star.screensize(1500, 1500)

star.reset()
star.color('red')
star.width(3)

star.home()
star.right(72)

star.begin_fill()
for x in range(1, 6):
    star.left(144)
    star.forward(200)

star.end_fill()
star.home()
sleep(1)
star.color('cyan')
star.circle(105.3)

star.home()
sleep(1)
star.color('violet')


star.forward(182.21)
star.left(120)
star.forward(364.4)
star.left(120)
star.forward(364.4)
star.left(120)
star.forward(182.21)


star.forward(182.21)
sleep(1)
star.color('black')

for x in range(1, 5):
    star.right(90)
    star.forward(364.4)


star.mainloop()
