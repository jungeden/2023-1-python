#ex7_6
'''
0에서 10까지의 정수의 제곱근 출력하기
'''
import math as m
for i in range(1, 11):
    print(f'sqrt({i}) = {m.pow(i, 0.5):.3f}')
