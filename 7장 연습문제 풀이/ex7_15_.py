#ex7_15
'''
추상화 그리기
'''
#2
import turtle as t
import random as rd

colors = ['red', 'blue', 'green', 'grey', 'pink', 'yellow']
shape = ['circle', 'square', 'triangle']

t.penup()

t.bgcolor('black')

d= 300

for _ in range(40):
    x = rd.randint(-d, d)
    y = rd.randint(-d, d)
    z = rd.randrange(0, 6)
    t.color(colors[z])
    t.shape(shape[rd.randint(0, 2)])
    t.shapesize(rd.randint(1,7))
    t.goto(x, y)
    t.stamp()

t.done()
