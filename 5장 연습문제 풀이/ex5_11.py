#ex5_11
'''
리스트 합, 평균, 최댓값, 최솟값 구하기
'''

n = list(map(int,input('5개의 수를 입력하세요 :').split()))
print(f'합 : {sum(n)}\n평균 : {sum(n)/len(n)}\n최댓값 : {max(n)}\n최솟값 : {min(n)}') #합,평균,최댓값,최솟값
