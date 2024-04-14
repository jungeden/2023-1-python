#ex3_22
n=12
for j in range(2,n+1):
    if j==2 or j==3: #2,3인 경우 
        print(' {} : 소수'.format(j))
    elif j%2 == 0: #2로 떨어질 경우 
        if j<10:
            print(' {} : 합성수'.format(j))
        else:
            print('{} : 합성수'.format(j))
    else:            
        for i in range(3,j): #2로 안떨어질 경우 3부터 자기 자신보다 1작은 수로 나눴을 때 
            if j%i != 0: #나누어 떨어지지 않을 경우 
                if j<10:
                    print(' {} : 소수'.format(j))
                else:
                    print('{} : 소수'.format(j))
                break
            elif j%i == 0: #나누어 떨어질 경우 
                if j<10:
                    print(' {} : 합성수'.format(j))
                else:
                    print('{} : 합성수'.format(j))
                break

    

          


                
    
    
