#5_22
'''
뱀행렬 문제를 리스트 슬라이싱을 사용해 풀기
'''
n_a=[]
n=int(input('n을 입력하시오 :'))
for i in range(1,(n**2)+1):
    if a%2 != 0:
        print(f'{i:2d}\n')
    else:
        print(f'{}')


        
    for j in range(1,n+1):
        j = j+1
        n_a.append(j)
        if i%2 != 0:
            print(f'{n_a}',end= ' ')
        else:
            print(f'{n_a[::-1]}',end= ' ')
        

#?????????/
    


