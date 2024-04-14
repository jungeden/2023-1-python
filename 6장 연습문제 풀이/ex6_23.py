#ex6_23
'''
문자열 슬라이싱 기능과 반복문을 사용하여 출력하기
'''
import string
s=string.ascii_uppercase #a부터 z까지 출력
for i in range(len(s[:10])): #j까지 끊기 
    print(s[i:]+s[:i])
