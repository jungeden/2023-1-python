#ex7_7
'''
math 모듈과 터틀 그래픽으로 다음 구하기
'''
#4
import math as m
import turtle as t

t=t.Turtle()
for i in range(4):
    t.fd(500)
    t.fd(-500)
    t.lt(90)

t.penup()
t.goto(-360,0)
t.pendown()
t.color('red')
for i in range(-360,360):
    y = m.sin(m.radians(i))
    t.goto(i,y*100)

t.penup()
t.goto(-360,100)
t.pendown()
t.color('blue')
for i in range(-360,360):
    y = m.cos(m.radians(i))
    t.goto(i,y*100)
