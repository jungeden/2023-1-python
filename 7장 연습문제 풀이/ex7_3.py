#7_3
'''
여러 함수들이 100번 수행하는데 소요되는 시간 출력하기
'''
import time
#1
def p_hp():
    s=0
    for i in range(100):
        print('Hello Python!\n')
t1 = time.time()
p_hp()
t2 = time.time()
print(f'Hello Python! 출력을 100번 반복하는 시간: {t2-t1:.4f}초')

#2
def f_1000():
    import math
    for i in range(100):
        math.factorial(1000)
t1 = time.time()
f_1000()
t2 = time.time()
print(f'1000!을 100번 반복해서 구하는 시간: {t2-t1:.4f}초')

#3
def t_1000():
    for i in range(100):
        a=0
        for j in range(1,1001,2):
            a+=j**3
t1 = time.time()
t_1000()
t2 = time.time()
print(f'1에서 1000까지 홀수의 세제곱 더하기를 100번 반복하는 시간: {t2-t1:.4f}초')       

#4
def sin_360():
    import math
    for i in range(100):
        b=0
        for i in range(1,361):
            b+=math.sin(math.radians(i))
t1 = time.time()
sin_360()
t2 = time.time()
print(f'1에서 360도까지 sin값의 합을 100번 반복하는 시간: {t2-t1:.4f}초')
