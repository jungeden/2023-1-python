#ex3_27
armstrong=[]
for n in range(100,1000):
    if n == ((n//100)**3 + (n//10%10)**3 + (n%10)**3): #각 자리수 세제곱의 합과 같다면 
        armstrong.append(n)                            #armstrong에 저장 

print('세 자리의 암스트롱 수 : {}'.format(armstrong))            
            
            
        
