#lab 7_4

#1
import math as m
for i in range(2,11):
    print(f'4**{i:2} = {int(m.pow(4,i)):8d}')


#2
for i in range(0,181,10):
    print(f'{i:3d}degree = {m.radians(i):5.3f} radian')

#3
for i in range(0,181,10):
    print(f'sin({i:4d}) = {m.sin(m.radians(i)):4.2f}')
