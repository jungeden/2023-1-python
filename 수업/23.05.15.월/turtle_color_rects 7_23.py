#turtle_color_rects 7_23

import turtle as t

colors = ['red','green','blue','orange']
for i in range(200):
    t.pencolor(colors[i%4])
    t.forward(i)
    t.left(93)
t.bgcolor('black')
t.speed(0)

t.done()    
