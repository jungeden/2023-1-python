#ex5_24
'''
1에서 10000까지의 모든 완전수와 진약수, 진약수의 합 구하기
'''
for i in range(1,10001):
    a_list=[]
    for j in range(1,i):
        if i%j==0:
            a_list.append(j)
    if sum(a_list)==i:        #같으면 완전수
        print(i,'은 완전수입니다.')
        print('{}의 약수 : {}, 약수의 합 = {}'.format(i,a_list,sum(a_list)))
