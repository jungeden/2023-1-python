#turtle_circle_with_for

import turtle as t

n=100
length = 5
for i in range(n):
    t.left(360/n)
    t.forward(length)

t.done()    
