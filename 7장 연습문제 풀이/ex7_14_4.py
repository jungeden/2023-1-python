#ex7_14
'''
범위 내에서만 움직이도록 코드 수정하기
'''
#4
from turtle import *
from random import *

turtles = [Turtle() for x in range(6)] # 거북이 6마리
colors = ['black','red','blue','green','grey','pink']

for i in range(6):
    t = turtles[i]
    t.pencolor(colors[i])
    t.shape('turtle')
    t.color(colors[i])
    t.penup()

    for _ in range(20):
        if abs(t.xcor()) > 400 or abs(t.ycor()) > 400:
            t.goto(0, 0)
        t.stamp()
        t.right(randrange(0, 361))
        t.fd(randrange(1, 101))

speed(0)
