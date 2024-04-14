#ex6_14_수정
'''
버블 정렬 문제를 단계별로 나타내기
'''
a_list = [5,6,31,9,2,12,13,8,7]
b_list = []
print(f'정렬전 리스트 = {a_list}')
 
for j in range(0,len(a_list)-1):
    for i in range(0,len(a_list)-1):
        if a_list[i] > a_list[i+1]:
            a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
    b_list.append(a_list[i+1])
    print(f'{j+1}단계 :{a_list}{b_list}')
print(f'정렬된 리스트 : {a_list}')

#??
