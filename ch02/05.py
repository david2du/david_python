#03.py - Draw a colorful spiral_add 4 color background color black
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = 6
#side : 2 ~ 6
color = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(1000):
    t.pencolor(color[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)