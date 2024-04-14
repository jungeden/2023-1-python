#ex3_31


for i in range(1,20000):
    a=0
    for j in range(1,i):
        if i%j==0: #나누어 떨어질 경우 약수 
            a=a+j  #약수일 경우 더함 
    b=0
    for k in range(1,a):
        if a%k==0:  
            b=b+k

    if i == b and i != a: #본인이 아닌 수 
        print('{}의 친화수 {}'.format(i,a))

            
