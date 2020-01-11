#04.py - Draw a square spiral_add 4 color background color black
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
color = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(color[x % 4])
    t.forward(x)
    t.left(91)