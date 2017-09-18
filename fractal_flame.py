import random
import turtle


r = lambda: random.randint(0, 255)


# calculate coefficients
def coefs(eqCount, range):
    all_coef = list()
    while len(all_coef) <= eqCount:
        # fill dict
        coef = {key: random.uniform(-range, range) for key in ['a', 'b', 'c', 'd', 'e', 'f']}
        #set color
        coef['color'] = r(), r(), r()
        # check if coefficient match to conditions
        if ((coef['a'] ** 2 + coef['d'] ** 2) < 1
            and (coef['b'] ** 2 + coef['e'] ** 2) < 1
            and (coef['a'] ** 2 + coef['b'] ** 2 + coef['d'] ** 2 + coef['e'] ** 2)
                < 1 + (coef['a'] * coef['e'] - coef['b'] * coef['d']) ** 2):
            all_coef.append(coef)
    return all_coef


# create dots array
def render(n, eqCount, it, xRes, yRes):
    pixels = {}
    coef = coefs(eqCount, 1)
    XMIN = -1.777
    XMAX = 1.777
    YMIN = -1
    YMAX = 1

    for num in range(0, n):
        newX = random.uniform(XMIN, XMAX)
        newY = random.uniform(YMIN, YMAX)
        for step in range(-20, it):
            i = random.randint(0, eqCount)
            newX = coef[i]['a'] * newX + coef[i]['b'] * newY + coef[i]['c']
            newY = coef[i]['d'] * newX + coef[i]['e'] * newY + coef[i]['f']
            if step >= 0:
                # calculate coordinates
                x1 = xRes - int(((XMAX - newX) / (XMAX - XMIN)) * xRes)
                y1 = yRes - int(((YMAX - newY) / (YMAX - YMIN)) * yRes)
                # if dot in screen
                if x1 < xRes and y1 < yRes:
                    # if dot in array
                    if not pixels.get((x1, y1)):
                        # add color and counter to coordinates
                        pixels[(x1, y1)] = {'color': (coef[i]['color']), 'counter': 1}
                    else:
                        # set color
                        pixels[(x1, y1)]['color'] = tuple(int((pixels[(x1, y1)]['color'][n] + coef[i]['color'][n]) / 2)
                                                          for n in range(3))
                        # increase dots counter
                        pixels[(x1, y1)]['counter'] += 1
    return pixels


# draw the dots
def draw():
    anton = turtle.Turtle()
    screen = turtle.Screen()
    screen.colormode(255)
    anton.speed(0)
    anton.penup()
    dots = render(100, 10, 100, 400, 300)
    for i in dots.keys():
        anton.goto(i[0] - 400 / 2, i[1] - 300 / 2)
        anton.color(dots[i]['color'])
        anton.dot(3)

draw()
