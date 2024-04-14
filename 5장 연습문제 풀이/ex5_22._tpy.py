#ex5_22
'''
리스트 슬라이싱으로 뱀 행렬 만들기
'''
n = int(input('n을 입력하시오 : '))
a = 0
for i in range(n):
    b = []
    for j in range(n):
        a += 1
        b.append(a)
    if i % 2 == 1: #홀수 줄 
        b = b[::-1]
    for i in b:
        print('{:3d}'.format(i), end = '')
    print()

