#ex5_10
'''
가장 작은 값 구하기
'''

n_list=[10,20,30,50,60]
a=100
for i in n_list:
    if i < a:
        a = i
print(f'리스트 원소들 : {n_list}\n리스트 원소들 중 최솟값 : {a}')        
