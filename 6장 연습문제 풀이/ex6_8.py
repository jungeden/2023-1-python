#ex6_8
'''
tup에서 한 번 이상 나타나는 원소를 출력하기
'''
tup = (1,2,5,4,3,2,9,1,4,7,8,9,9)
dup = set()
for i in tup:
    if tup.count(i) > 1: #1개 이상일 때 
        dup.add(i)
print(f'주어진 튜플은 : {tup}\n중복 원소는 : {dup}')        
    
