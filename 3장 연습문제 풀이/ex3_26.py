#ex3_26

n=int(input('n을 입력하시오 :'))

if 1<n<10:                               #1보다 크고 10보다 작은 값 
    for i in range(1,n+1): 
        if i%2 != 0:         #홀수줄일 때 
            for j in range(n*(i-1)+1,(n*i)+1): 
                if j < 10:   #10보다 작은 경우 숫자 앞 공백 
                    print('',j,end=' ')
                else:         
                    print(j,end=' ')
            print()        
        else:                #짝수줄일 때
            for j in range(n*i,n*(i-1),-1):
                if j < 10:
                    print('',j,end=' ')
                else:
                    print(j,end=' ')

            print()
      
