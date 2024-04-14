#ex6_21
'''
회문인지 판별하는 코드 만들기
'''
a=input('문자열을 입력하시오 :')
a=a.lower()
a=a.replace(' ','')
a=a.replace('.','')

if a == a[::-1]: #같으면 
    print('회문입니다.')
else: #다르면 
    print('회문이 아닙니다.')
