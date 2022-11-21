import colorgram
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

color_list = [
    (132, 166, 205),
    (221, 148, 106),
    (32, 42, 61),
    (199, 135, 148),
    (166, 58, 48),
    (141, 184, 162),
    (39, 105, 157),
    (237, 212, 90),
    (150, 59, 66),
    (216, 82, 71),
    (168, 29, 33),
    (235, 165, 157),
    (51, 111, 90),
    (35, 61, 55),
    (156, 33, 31),
    (17, 97, 71),
    (52, 44, 49),
    (230, 161, 166),
    (170, 188, 221),
    (57, 51, 48),
    (184, 103, 113),
]

tim.speed(0)
tim.hideturtle()
tim.penup()

tim.setheading(225)
tim.forward(325)
tim.setheading(0)

for i in range(10):

    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
