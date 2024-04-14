#ex7_14
'''
터틀 그래픽 프로그램 만들기
'''
import turtle
import random

colors = ["black", "red", "blue", "green", "gray", "pink"]

def move_turtles():
   turtles = []
    for _ in range(6):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(random.choice(colors))
        turtles.append(t)
    for _ in range(20):
        for t in turtles:
            distance = random.randint(1, 100)
            angle = random.randint(0, 360)
            t.forward(distance)
            t.right(angle)

    turtle.done()

move_turtles()
