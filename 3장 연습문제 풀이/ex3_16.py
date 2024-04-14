#ex3_16

n=int(input('1에서 9까지의 수를 입력하세요 :'))
while n<=0 or n>9: #0이나 9이상의 수를 입력한 경우
    n=int(input('1에서 9까지의 수를 다시 입력하세요 :'))

else:
    for i in range(1,10):
            print(n,'*',i,'=',n*i)
