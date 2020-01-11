#03.py - Draw a circle spiral_add 4 color background color black
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
color = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(color[x % 4])
    t.circle(x)
    t.left(91)