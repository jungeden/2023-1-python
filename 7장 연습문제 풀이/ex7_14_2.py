#7_14
'''
거북이 그림 나타내기
'''
#2
from turtle import *
from random import *

turtles = [Turtle() for x in range(6)]
colors = ['black','red','blue','green','grey','pink']

for i in range(6):
    t = turtles[i]
    t.pencolor(colors[i])
    t.shape('turtle')
    t.color(colors[i])

    for _ in range(20):
        t.stamp()
        t.right(randrange(0, 361))
        t.forward(randrange(1, 101))

speed(0)
