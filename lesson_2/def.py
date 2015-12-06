from random import randint


def greeting():
    print('Hello')

greeting()


def height(m, cm):
    total = (100 * m) + cm
    print(total, 'cm total')

height(4, 88)


def num_input(prompt):
    typed = input(prompt)
    num = int(typed)
    return num

a = 7  # num_input('Enter a')
b = 8  # num_input('Enter b')
print('a + b =', a + b)


name = ['Alex', 'Lee', 'Sam']
verb = ['buys', 'rides', 'kicks']
noun = ['lion', 'bicycle', 'plane']


def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked

print(pick(name), pick(verb), pick(noun), end='.\n')

while True:
    print(pick(name), pick(verb), pick(noun), end='.\n')
    input()

