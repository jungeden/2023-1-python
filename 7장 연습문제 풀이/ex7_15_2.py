#ex7_15_2
import turtle as t
import random as rd

t.bgcolor("black")
t.speed(0)
t.shape('circle')
t.shapesize(rd.randint(10, 50))

t.penup()
d = 300
colors = ['red', 'blue', 'green', 'gray', 'pink', 'yellow']
for i in range(60):
    t.color(colors[i % 6])
    x = rd.randint(-d, d)
    y = rd.randint(-d, d)
    t.goto(x,y)
    t.shapesize(rd.randint(1, 5))
    t.stamp()
