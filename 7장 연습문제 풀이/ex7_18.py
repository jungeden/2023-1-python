#ex7_18
'''
원 패턴 5방향으로 그리기
'''
import turtle as t
t.bgcolor('black')
t.speed(0)

colors = ["cyan", "orange", "yellow", "white", "red"] #색
for i in range(5): #5개 
    t.color(colors[i])
    t.setheading(72 * i)
    for j in range(1, 11):
        t.circle(10 * j)
