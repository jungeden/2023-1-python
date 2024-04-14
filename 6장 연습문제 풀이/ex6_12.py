#ex6_12
'''
가장 큰 값 12를 마지막으로 옮기기
'''
a_list = [5,6,3,9,2,12,3,8,7]
print(f'주어진 리스트는 = {a_list}')
for i in range(0,len(a_list)-1):
    if a_list[i] > a_list[i+1]: #큰 수 찾기
        a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
print(f'가장 큰 수를 마지막으로 옮긴 결과 :{a_list}')
      
