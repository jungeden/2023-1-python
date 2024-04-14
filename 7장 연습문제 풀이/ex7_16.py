#ex7_16
'''
exit 그리기
'''
import turtle as t
t.clearscreen()
t=t.Turtle()
t.shape('turtle')
t.speed(10)

# E 
t.penup()
t.setpos(-200, 100)

t.pendown()
for E in range(2):
  t.right(180)
  t.forward(100)
  t.left(90)
  t.forward(80)
  t.left(90)
  t.forward(100)

# X
t.penup()
t.setpos(-100, 20)
t.right(45)

for X in range(4):
  t.pendown()
  t.right(90)
  t.forward(100)
  t.right(180)
  t.forward(100)

# I
t.penup()
t.setpos(30, 100)
t.right(45)
t.pendown()
t.forward(160)

# T
t.penup()
t.setpos(100, 100)
t.left(90)
t.pendown()

for T in range(1):
  t.forward(130)
  t.right(180)
  t.forward(65)
  t.left(90)
  t.forward(160)
