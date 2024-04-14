#ex6_24_1,2,3,4,5
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

#3
z=''
s=input('문장을 입력하시오 :')
for i in s:
    if i in src_str: #A-Z 중 있으면 
        z+=(ciper(i,1)) #추가
    else: #알파벳 아니면 
        z+=i #그대로 
print(f'암호화된 문장: {z}')        

#4
x=''
c_s=input('암호화된 문장을 입력하시오 :')
for i in c_s:
    if i in src_str: 
        x+=src_str[dst_str.index(i)] #D->0->A
    else:
        x+=i
print(f'해독화된 문장: {x}')      

#5
import string
src_str = string.ascii_uppercase + string.ascii_lowercase
dst_str = src_str[3:26]+src_str[0:3]+src_str[29:]+src_str[26:29] #DEFGHIJKLMNOPQRSTUVWXYZ + ABC + defghijklmnopqrstuvwxyz + abc

z=''
s=input('문장을 입력하시오 :')
for i in s:
    if i in src_str: #A-Z에서 있으면 
        z+=(ciper(i,1)) #추가
    else: #알파벳 아니면 
        z+=i #그대로 
print(f'암호화된 문장: {z}')

x=''
c_s=input('암호화된 문장을 입력하시오 :')
for i in c_s:
    if i in src_str: 
        x+=dst_str[src_str.index(i)] #V->22->Y
    else:
        x+=i
print(f'해독화된 문장: {x}')  
