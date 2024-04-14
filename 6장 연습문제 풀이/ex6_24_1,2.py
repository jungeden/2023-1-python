#ex6_24_1,2
'''
카이사르 암호를 활용해 출력하기
'''
#1
import string
src_str = string.ascii_uppercase
dst_str = src_str[3:]+src_str[:3]

print(f'src_str = {src_str}\ndst_str = {dst_str}')
print()

#2
def ciper(a,b): #a = 변환할 문자 b = 0 or 1
    if b == 0: #0이면 문자의 인덱스 출력 
        return src_str.index(a)
    elif b == 1: #1이면 인덱스에 해당하는 dst_str 문자 출력 
        return dst_str[src_str.index(a)]

print(f'src_str의 A 인덱스 : {ciper("A",0)}\ndst_str의 {ciper("A",0)}번째 알파벳 : {ciper("A",1)}') #A
print(f'src_str의 B 인덱스 : {ciper("B",0)}\ndst_str의 {ciper("B",0)}번째 알파벳 : {ciper("B",1)}') #B
