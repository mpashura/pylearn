
a = 2
b = a
print('a =', a, 'b =', b)

a = 100
print('a =', a, 'b =', b)

listA = [1, 2, 3]
listB = listA
print('listA =', listA, 'listB =', listB)

listA[1] = 1000
print('listA =', listA, 'listB =', listB)

listB[2] = 75
print('listA =', listA, 'listB =', listB)


def func1():
    c = 10
    print(c)

func1()

d = 2000


def func2(y):
    print(y)
    y = 'bread'
    print(y)

z = 'butter'
func2(z)
print(z)
