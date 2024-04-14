#ex5_12
'''
n을 입력 받은 후 합, 평균, 최댓값, 최솟값 구하기
'''

n=int(input('n을 입력하세요 :'))
num=list(map(int,input(f'{n}개의 수를 입력하세요 :').split()))
print(f'합 : {sum(num)}\n평균 : {sum(num)/len(num)}\n최댓값 : {max(num)}\n최솟값 : {min(num)}')#합,평균,최댓값,최솟값
