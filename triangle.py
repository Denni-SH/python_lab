import turtle

anton = turtle.Turtle()
turtle.Screen()


def triangle(lenght, split):
    if split == 0:
        anton.begin_fill()
        anton.forward(lenght)
        anton.left(120)
        anton.forward(lenght)
        anton.left(120)
        anton.forward(lenght)
        anton.left(120)
        anton.end_fill()
    else:
        triangle(lenght/2, split-1)
        anton.forward(lenght/2)
        triangle(lenght/2, split-1)
        anton.left(120)
        anton.forward(lenght/2)
        anton.right(120)
        triangle(lenght/2, split-1)
        anton.right(120)
        anton.forward(lenght/2)
        anton.left(120)


def paint(x, y, lenght, split, fill_col):
    anton.color('white')
    anton.setposition(x, y)
    anton.color('black', fill_col)
    triangle(lenght, split)

paint(-200, -150, 400, 2, 'green')
input('that`s it')
