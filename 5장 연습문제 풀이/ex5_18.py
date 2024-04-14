#5_18
'''
s_list = ['abc','bcd','bcdefg','abba','cddc','opq'] 리스트에 대해 기능 구현하기
'''
#1
s_list = ['abc','bcd','bcdefg','abba','cddc','opq']

n = 10
for i in range(0,6):
    if len(s_list[i]) < n: #길이 비교 
        n = len(s_list[i]) #작으면 저장 
        a = s_list[i]
print(f'가장 길이가 짧은 문자열 : {a}')

#2
s_list = ['abc','bcd','bcdefg','abba','cddc','opq']

x = 0
for i in range(0,6): 
    if len(s_list[i]) > x:  
        x = len(s_list[i])  
        b = s_list[i] 
print(f'가장 길이가 긴 문자열 : {b}') 

#3
s_list = ['abc','bcd','bcdefg','abba','cddc','opq']
s_list.sort(key=len)

for i in range(0,6):
    if len(s_list[i]) <= n:
        n = len(s_list[i])
        c = s_list[i]
print(f'가장 길이가 짧은 문자열 : {c}')        
        
     
    
        
    
