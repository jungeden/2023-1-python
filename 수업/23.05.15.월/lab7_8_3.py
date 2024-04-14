#lab7_8
#3
import turtle as t
colors = ['blue','red','yellow','green']
def draw_rect(i):
    t.setheading(90*i)
    t.color(colors[i])
    t.circle(20)
for i in range(4):
    draw_rect(i)

t.done()
