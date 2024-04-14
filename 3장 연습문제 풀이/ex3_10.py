#ex3_10
a,b=map(int,input('두 정수를 입력하시오 :').split())


if a%b == 0: #a를 b로 나눴을 때 나머지 
    print(a,'는(은)',b,'의 배수입니다.')
else:
    print(a,'는(은)',b,'의 배수가 아닙니다.')
