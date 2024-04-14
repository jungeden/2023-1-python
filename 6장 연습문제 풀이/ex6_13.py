#ex6_13
'''
거품정렬 구현하기
'''
a_list = [5,6,3,9,2,12,3,8,7]
print(f'주어진 리스트는 = {a_list}')
 
for j in range(0,len(a_list)-1):
    for i in range(0,len(a_list)-1):
        if a_list[i] > a_list[i+1]:
            a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
print(f'정렬된 결과는 :{a_list}')
