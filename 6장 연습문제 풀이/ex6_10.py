#ex6_10
'''
가장 많이 나타내는 요소가 두 개 이상일 경우 더 큰 값 출력하기
'''

#1
tup = (1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)

a=0

for i in tup:
    if tup.count(i) > tup.count(a): #비교
        a=i
    elif tup.count(i) == tup.count(a): #같으면 큰 값
        a=max(i,a)

print(f'주어진 튜플은 : {tup}\n가장 많이 나타나는 요소는 : {a}')

        
#2
tup = (1,2,5,4,3,2,9,4,7,8,9,9,3,7,3)

a=0

for i in tup:
    if tup.count(i) > tup.count(a):
        a=i
    elif tup.count(i) == tup.count(a):
        a=max(i,a)

print(f'주어진 튜플은 : {tup}\n가장 많이 나타나는 요소는 : {a}')
        
    
