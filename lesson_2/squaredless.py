import turtle as sq

#  sq.width(2)

print(range(0, 4))


def mysquare(size):
    for x in range(0, 4):
        if x % 2 == 0:
            sq.color('red')
            sq.forward(size)
            sq.left(90)
        else:
            sq.color('green')
            sq.forward(size)
            sq.left(90)


def mysquare2(size):
    for x in range(0, 4):
        if x % 2 == 0:
            sq.color('green')
            sq.forward(size)
            sq.left(90)
        else:
            sq.color('red')
            sq.forward(size)
            sq.left(90)

for y in range(0, 100, 5):
    mysquare(y)

sq.mainloop()


