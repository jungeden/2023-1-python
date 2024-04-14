#lab7_9
#1
import turtle as t
import random as rd

t.shape('turtle')
t.shapesize(4,4)
d = 300
t.penup()
for i in range(40):
    x = rd.randint(-d,d)
    y = rd.randint(-d,d)
    t.goto(x,y)
    t.stamp()

t.done()    
