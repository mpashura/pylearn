from turtle import *

# dr.mainloop()


def turtle_controller(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup(val)
    elif do == 'D':
        pendown(val)
    elif do == 'N':
        reset()
    else:
        print('Unrecognized command')

# turtle_controller('F', 100)
# turtle_controller('R', 90)
# turtle_controller('B', 45)

programs = 'N-L90-F100-R45-F70-R90-F70-R45-F100-R90-F100'
cmd_lists = programs.split('-')
print(cmd_lists)


def string_artist(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        turtle_controller(cmd_type, num)

# string_artist('N-L90-F100-R45-F70-R90-F70-R45-F100-R90-F100')

instructions = '''Enter the program for the turtle
blah blah blah
'''
screen = getscreen()
while True:
    t_program = screen.textinput('Drawing machine', instructions)
    print(t_program)
    if t_program is None or t_program.upper() == 'END':
        break
    string_artist(t_program)


