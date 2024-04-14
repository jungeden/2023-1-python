#ex6_24
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
def ciper(a): #함수 
    if type(a) == str:
        return src_str.index(a)
    elif type(a) == int:
        return dst_str[a]
print(f'src_str의 A 인덱스 : {ciper("A")}')
print(f'dst_str의 0번째 알파벳 : {ciper(0)}')
print(f'src_str의 B 인덱스 : {ciper("B")}')
print(f'dst_str의 1번째 알파벳 : {ciper(1)}')
print()
#3
decode_str=input('문장을 입력하시오: ')
encode_str=''
for i in decode_str:
    if i in src_str:   
        encode_str+=ciper(ciper(i))
    else:   #공백,느낌표            
        encode_str+=i
print(f'암호화된 문장: {encode_str}')
print()
#4
encode_str=input('암호화된 문장을 입력하시오:')
decode_str=''
for i in encode_str:
    if i in src_str:   
        decode_str+=src_str[dst_str.index(i)]   
    else:              
        decode_str+=i
print(f'해독화된 문장: {decode_str}')
print()
#5
import string    
src_str = string.ascii_uppercase + string.ascii_lowercase
dst_str = ''
for i in src_str[3:26]:   # DEFGHIJKLMNOPQRSTUVWXYZ
    dst_str += i
for i in src_str[:3]:     # ABC
    dst_str += i
for i in src_str[29:]:    # dcfghijklmnopqrstuvwzyx 
    dst_str += i
for i in src_str[26:29]:  # abc
    dst_str += i

decode_str=input('문장을 입력하시오: ')
encode_str=''
for i in decode_str:
    if i in src_str:   
        encode_str+=dst_str[src_str.index(i)]
    else:              
        encode_str+=i
print(f'암호화된 문장: {encode_str}')
