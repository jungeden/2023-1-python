#ex6_9
'''
중복된 요소를 한 번만 출력되도록 수정한 튜플 생성하기
'''
tup = (1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)
dup = set(tup) #set함수 
dup = tuple(dup) #tuple함수 

print(f'주어진 튜플 : {tup}\n중복 제거 튜플 : {dup}') 
