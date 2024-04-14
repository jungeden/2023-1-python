#ex5_9
'''
가장 큰 값
'''

n_list=[10,20,30,50,60]
a=1
for i in n_list:
    if i > a:
        a = i
print(f'리스트 원소들 : {n_list}\n리스트 원소들 중 최댓값 : {a}')        
