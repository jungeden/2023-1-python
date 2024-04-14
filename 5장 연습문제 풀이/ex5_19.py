#ex5_19
'''
리스트에서 중복하여 나타나는 'abc'와 'opq'를 제거한 리스트 new_s_list를 생성하기
'''
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for v in s_list: #리스트에 포함되지 않는 것 추가 
    if v not in new_s_list:
        new_s_list.append(v)

print("s_list =", s_list)
print("new_s_list =", new_s_list)
