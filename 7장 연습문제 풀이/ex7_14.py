#7_14
'''
거북이 궤적 나타나지 않게 수정하기 
'''
#3
from turtle import *
from random import *

turtles = [Turtle() for x in range(6)]
colors = ['black','red','blue','green','grey','pink']

for i in range(6):
    t = turtles[i]
    t.pencolor(colors[i])
    t.shape('turtle')
    t.color(colors[i])
    t.penup()

    for _ in range(20):
        t.stamp()
        t.right(randrange(0, 361))
        t.forward(randrange(1, 101))

