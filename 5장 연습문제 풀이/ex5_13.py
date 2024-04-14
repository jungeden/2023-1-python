#ex5_13
'''
n을 입력 받은 후 평균과 표준편차 구하기
'''
n=list(map(int,input(f'10개의 수를 입력하세요 :').split()))
a=0
for i in n:
    a+=((i-(sum(n)/len(n)))**2)
print(f'합 : {sum(n)}\n평균 : {sum(n)/len(n)}\n표준편차 :{(a/len(n))**0.5:2f}')
