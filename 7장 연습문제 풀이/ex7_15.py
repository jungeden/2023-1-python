#ex7_15
'''
추상화 그리기
'''
#1
import turtle as t
import random as rd

t.shape('circle')
d=300
t.penup()
color = ['red','blue','green','gray','pink','yellow']
for i in range(60):
    t.color(colors[i%6])
    x = rd.randint(-d,d)
    y = rd.randint(-d,d)
    t.goto(x,y)
    t.stamp()
    t.shapesize(a,b)
    
t.bgcolor('black')
t.speed(0)

t.done()    
