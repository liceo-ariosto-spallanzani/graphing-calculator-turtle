from turtle import *

SIZE = 200
SAMPLE_SIZE = 400

def draw_line(a, b):
    goto(a)
    pendown()
    goto(b)
    penup()

def f(x):
    return 3*x + 2

def init():
    speed(100)
    color("black")
    draw_line((-SIZE, 0), (+SIZE, 0))
    draw_line((0, -SIZE), (0, +SIZE))

color("red")
for x in range(-SIZE, +SIZE):
    goto(x, f(x))
    pendown()