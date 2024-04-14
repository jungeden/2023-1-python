#ex7_7
'''
math 모듈과 터틀 그래픽으로 다음 구하기
'''
#1
import math as m
for i in range(1,301,30):
    print(f'log{(i)}={m.log(i,m.e):.3f}')

#2
import turtle as t

t=t.Turtle()
for i in range(4):
    t.fd(500)
    t.fd(-500)
    t.lt(90)
t.penup()
t.goto(0,0)
t.pendown()
t.color("red")

for i in range(1,301,30):
    x=i
    y=m.log(i,m.e)
    t.goto(x,y)



