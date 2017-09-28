
def circle(anton,x, y, radius, vector):
        anton.penup()
        anton.setposition(int(x),int(y))
        anton.pendown()
        if vector == 'up':
            anton.circle(int(radius))
        elif vector == 'down':
            anton.circle(-int(radius))

def triangle(anton,x, y, a,b, angle_right, angle_right2): # not 180 or 360
    anton.penup()
    anton.setposition(int(x),int(y))
    anton.pendown()
    anton.right(int(angle_right))
    anton.forward(a)
    anton.right(int(angle_right2))
    anton.forward(b)
    anton.setposition(int(x),int(y))


def rectangle(anton,x, y, a,b, angle_right, vector):
    anton.penup()
    anton.setposition(int(x),int(y))
    anton.pendown()
    anton.right(int(angle_right))
    for i in range(0,2):
        anton.forward(int(a))
        if vector == 'right':
            anton.right(90)
        elif vector == 'left':
            anton.left(90)
        anton.forward(int(b))
        if vector == 'right':
            anton.right(90)
        elif vector == 'left':
            anton.left(90)

def line(anton,x, y, len, angle_right):
    anton.penup()
    anton.setposition(int(x),int(y))
    anton.pendown()
    anton.right(int(angle_right))
    anton.forward(int(len))

