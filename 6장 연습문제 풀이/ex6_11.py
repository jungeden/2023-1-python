#ex6_11
'''
빈 튜플, 문자열, 리스트 제거하기
'''
a_list=[(),1,(),(),(1),('a',),('a','b'),((),),('a','b'),'']
a=[]
for i in a_list:
    if i!=() and i!=[] and i!='': #빈 요소 아니면 추가 
        a.append(i)

print(f'주어진 리스트 : {a_list}\n빈 튜플 요소를 제거한 결과 : {a}')        
