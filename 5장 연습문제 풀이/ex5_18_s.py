#5_18_s
'''
 s_list = [‘abc’, ‘bcd’, ‘bcdefg’, ‘cddc’, ‘opq’]와 같은 문자열을 가진 리스트가 존재한다. 이 리스트에 대하여 다음과 같은 기능을 구현하라.
'''

#1
s_list = ['abc','bcd','bcdefg','cddc','opq']
lst = list(zip(s_list,[len(v) for v in s_list]))

minimum = lst[0]
for v in lst:
    if v[1] < minimum[1]:
        minimum = v
print('가장 길이가 짧은 문자열 :',minimum[0])

#2
s_list = ['abc','bcd','bcdefg','cddc','opq']
lst = list(zip(s_list,[len(v) for v in s_list]))

maximum = lst[0]
for v in lst:
    if v[1] > maximum[1]:
        maximum = v
print('가장 길이가 긴 문자열 :',maximum[0])

#3
s_list = ['abc','bcd','bcdefg','cddc','opq']
s_list.sort(key=len)
s_list = list(filter(lambda x : len(x) == len(s_list[0]),s_list))
print('가장 길이가 짧은 문자열 :',s_list)
