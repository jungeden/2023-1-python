#ex3_9

n=int(input('정수를 입력하시오 :'))
if n%2 != 0: #2 나누기
    print(n,'는(은) 2(으)로 나누어지지 않습니다.')
else:
    print(n,'는(은) 2(으)로 나누어집니다.')
if n%3 != 0: #3 나누기 
    print(n,'는(은) 3(으)로 나누어지지 않습니다.')
else:          
    print(n,'는(은) 3(으)로 나누어집니다.')
if n%2 == 0 and n%3 == 0: #2,3 나누기 
    print(n,'는(은) 2와(과) 3모두로 나누어집니다.')     
else:
    print(n,'는(은) 2와(과) 3모두로 나누어지지 않습니다.')     
