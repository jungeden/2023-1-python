#3-27.
n= int(input('합계를 구할 수를 입력하세요 :'))
s = 0

for i in range(0,n):
    s = s + (i+1)

print('1부터 {}까지의 합은{}'.format(n,s))

#3-28.
n= int(input('합계를 구할 수를 입력하세요 :'))
s = 0

for i in range(1,n+1):
    s = s + i

print('1부터 {}까지의 합은{}'.format(n,s))

