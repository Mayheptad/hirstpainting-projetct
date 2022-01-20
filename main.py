import turtle
from turtle import Turtle, Screen
from random import choice, randint as rdt
import colorgram as cg

tr = Turtle()
sr = Screen()


# hirst paint
# extract_color = cg.extract('hirstpaint.jpg', 30)

extracted_colors = [(224, 225, 213), (207, 212, 208), (20, 21, 29), (194, 163, 117), (158, 81, 41), (204, 211, 215),
                    (142, 168, 186), (181, 160, 29), (220, 207, 113), (66, 101, 135), (154, 178, 165), (62, 37, 27),
                    (72, 117, 77), (152, 26, 15), (47, 31, 36), (185, 142, 154), (146, 67, 82), (209, 85, 61),
                    (223, 214, 216), (187, 89, 107), (88, 124, 178), (177, 200, 192), (88, 157, 89),
                    (233, 207, 10), (40, 54, 101), (78, 76, 31), (131, 31, 38), (34, 49, 41), (222, 180, 171),
                    (75, 147, 164)]

# for color in extract_color:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     extracted_colors.append(color_tuple)
#
# print(extracted_colors)

turtle.colormode(255)
tr.speed('fastest')

tr.hideturtle()
tr.setheading(225)
tr.penup()
tr.forward(300)
tr.setheading(360)


def draw_dot():
    for move in range(10):
        tr.dot(15, choice(extracted_colors))
        tr.forward(25)


def goto_next_line():
    tr.setheading(90)
    tr.forward(25)
    tr.setheading(180)
    tr.forward(250)
    tr.setheading(360)


def draw_hirst_painting():
    # draw_ten_circle()
    draw_dot()
    goto_next_line()


for dot in range(1, 11):
    draw_hirst_painting()


# def draw_ten_circle():
#     for move in range(10):
#         tr.color(choice(extracted_colors))
#         tr.circle(7)
#         tr.penup()
#         tr.forward(25)
#         tr.pendown()


# spirograph procedural
# turtle.colormode(255)
# tr.speed('fastest')
#
#
# def random_color():
#     r = rdt(0, 255)
#     g = rdt(0, 255)
#     b = rdt(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple
#
#
# for _ in range(100):
#     tr.color(random_color())
#     tr.circle(100)
#     tr.left(10)
#     # tr.setheading(tr.heading() + 10)


# spirograph Functional
# turtle.colormode(255)
# tr.speed('fastest')
#
#
# def random_color():
#     r = rdt(0, 255)
#     g = rdt(0, 255)
#     b = rdt(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tr.color(random_color())
#         tr.circle(100)
#         tr.setheading(tr.heading() + size_of_gap)
#
#
# draw_spirograph(5)


# triangle, square, decagon petagon dexagon etc (diffrent shape)

# colo_arr = ['green', 'red', 'purple', 'blue', 'yellow', 'brown', 'navy', 'aqua', 'violet', 'pink']

# for s in range(3, 11):
#     angle = 360 / s
#     tr.color(colo_arr[s-3])
#     for t in range(s):
#         tr.forward(100)
#         tr.right(angle)


# random walk
# turtle.colormode(255)

# def random_color():
#     r = rdt(0, 255)
#     g = rdt(0, 255)
#     b = rdt(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple

# tr.pensize(15)
# tr.speed('fastest')
# colo_arr = ['green', 'red', 'purple', 'blue', 'yellow', 'aqua', 'violet', 'pink']
# turnsDegree = [0, 90, 180, 270]

# for s in range(100000):
#     tr.color(random_color())
#     tr.forward(30)
#     tr.setheading(choice(turnsDegree))


# dashed line
# for _ in range(20):
#     tr.forward(5)
#     tr.penup()
#     tr.forward(5)
#     tr.pendown()
#     tr.forward(5)


#  triangle
# def draw_triangle():
#     tr.forward(100)
#     tr.right(120)
#     tr.forward(100)
#     tr.right(120)
#     tr.forward(100)
#     tr.right(120)

# square
# def draw_square():
#     tr.forward(100)
#     tr.right(90)
#     tr.forward(100)
#     tr.right(90)
#     tr.forward(100)
#     tr.right(90)
#     tr.forward(100)
#     tr.right(90)


# five side gon
# def draw_five_side_gon():
#     tr.forward(100)
#     tr.right(72)
#     tr.forward(100)
#     tr.right(72)
#     tr.forward(100)
#     tr.right(72)
#     tr.forward(100)
#     tr.right(72)
#     tr.forward(100)
#     tr.right(72)


# six side gon
# def draw_six_side_gon():
#     tr.forward(100)
#     tr.right(60)
#     tr.forward(100)
#     tr.right(60)
#     tr.forward(100)
#     tr.right(60)
#     tr.forward(100)
#     tr.right(60)
#     tr.forward(100)
#     tr.right(60)
#     tr.forward(100)
#     tr.right(60)

# draw_triangle()
# draw_square()
# draw_five_side_gon()
# draw_six_side_gon()


sr.exitonclick()
