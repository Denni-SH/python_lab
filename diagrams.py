import turtle
import random
import argparse


anton = turtle.Turtle()
turtle.Screen()
anton.speed(0)
r = lambda: random.randint(0, 255)


def circle_diagram(val_dict, length):
    l_colors = []
    anton.penup()
    anton.setposition(-100, 0)
    anton.pendown()
    buf_coord = 16,0
    for i in val_dict:
        l_colors.append('#%02X%02X%02X' % (r(), r(), r()))
        anton.color('black', l_colors[len(l_colors)-1])
        anton.begin_fill()
        anton.setposition(buf_coord)
        anton.right(90)
        for x in range(int(360/length*val_dict[i])):
            anton.forward(2)
            anton.right(1)
        buf_coord = anton.pos()
        anton.left(90)
        anton.setposition(-100, 0)
        anton.end_fill()
    return l_colors


def line_diagram(val_dict):
    l_colors = []
    for i in val_dict:
        anton.penup()
        anton.setposition(-110, 0)
        anton.pendown()
        l_colors.append('#%02X%02X%02X' % (r(), r(), r()))
        for j in range(val_dict[i]):
            anton.color(l_colors[len(l_colors)-1], 'black')
            anton.forward(50)
            anton.circle(3)
        anton.penup()
        anton.forward(35)
        anton.pendown()
        anton.write(i, move=True, align="left", font=("Arial", 12, "normal"))
        anton.right(360/len(val_dict))
    return l_colors


def show_list(val_dict, l_color):
    anton.penup()
    anton.setposition(140, 100)
    anton.pendown()
    buf = 0
    for i in val_dict:
        anton.color(l_color[buf], l_color[buf])
        anton.begin_fill()
        anton.circle(8)
        anton.penup()
        anton.forward(5)
        anton.pendown()
        anton.write('        ' + str(i) + " - " + str(val_dict[i]) + ' time(s)', font=("Arial", 12, "normal"))
        anton.end_fill()
        anton.penup()
        anton.backward(5)
        anton.setposition(anton.xcor(), anton.ycor()-40)
        anton.pendown()
        buf += 1
    input('Click enter ')


# def diagram_decorator(func):
#     def wrapper():
#         func()
#         print('just added decorator..nothing useful')
#     return wrapper()


def draw(f_text, type):
    val_list = f_text.split(' ')
    val_dict = {}
    for i in val_list:
        val_dict[i] = val_list.count(i)
    if type == 'd_circle':
        show_list(val_dict, circle_diagram(val_dict, len(val_list)))
    else:
        show_list(val_dict, line_diagram(val_dict))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('type', choices=["d_circle", "d_line"], help="Choose d_circle or d_line")
    parser.add_argument('str', help="Enter string")
    args = parser.parse_args()
    draw(args.str, args.type)

