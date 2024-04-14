#ex7_13
'''
체스판 그리기
'''
import turtle as t

grid=8      #격자 개수 
cb_size=400   #체스판 전체 크기
cb_turn=90
half_cb_size=cb_size/2
grid_size=cb_size/grid #격자 크기 지정 

colors=['black', 'white']

t.penup()
t.goto(-half_cb_size, -half_cb_size)
t.pendown()

for i in range(grid):
    for j in range(grid):
        t.color(colors[j%2])
        t.begin_fill()
        for k in range(4):
            t.forward(grid_size)
            t.left(cb_turn)
        t.end_fill()
        t.forward(grid_size)
    colors.reverse()  #black, white 패턴 반대로 
    t.penup()
    t.goto(-half_cb_size, -half_cb_size + grid_size*(i+1))
    t.pendown()

t.penup()
t.pensize(4) 
t.goto(-half_cb_size, -half_cb_size)
t.pendown()

for _ in range(4):
    t.forward(cb_size)
    t.left(cb_turn)

t.done()
