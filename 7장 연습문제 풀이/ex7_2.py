#ex7_2
'''
1부터 1,000,000까지 정수의 합을 구하는 함수 작성하기
'''
import time
def sum1to1000000(): #함수
    s=0
    for i in range(1,1000001): #1부터 1000000까지 
        s += i

#1
t1 = time.time() #시작 시간 
sum1to1000000()
t2 = time.time() #끝 시간

print(f'1에서 1,000,000까지의 합을 구한는 시간 : {t2-t1:.4f}초') #끝난 시간에서 시작 시간 뻄

#2
t1 = time.time()
for i in range(100):
    sum1to1000000()
t2 = time.time()

print(f'1,000,000까지의 합을 100번 반복해서 구하는 시간 : {t2-t1:.4f}초')
