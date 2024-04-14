#lab7_9
#2
import turtle as t
import random as rd

t.shape('turtle')
t.shapesize(4,4)
d = 300
t.penup()
colors = ['blue','red','yellow','green']
for i in range(40):
    t.color(colors[i%4])
    x = rd.randint(-d,d)
    y = rd.randint(-d,d)
    t.goto(x,y)
    t.stamp()

t.done()    
