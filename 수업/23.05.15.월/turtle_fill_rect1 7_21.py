#turtle_fill_rect1 7_21
 
import turtle as t

t.color('blue')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.done()
