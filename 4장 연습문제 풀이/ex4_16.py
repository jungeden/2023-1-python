#ex4_16

nums=map(int,input('쉼표로 구분된 정수를 여러 개 입력하시오 :').split(','))
a=[]

for i in nums: #정수 리스트 
    a.append(i)
print('입력된 정수의 리스트 : {}'.format(a))

a.sort() #정렬 
print('정렬된 정수의 리스트 :',end='')
for i in a:
    print(i,end=' ')



