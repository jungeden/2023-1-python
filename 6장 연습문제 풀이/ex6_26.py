#ex6_26
'''
정수를 입력받아 mylist튜플과 비교하기 
'''

mylist = [(1,2), (4,5), (4,2), (3,1), (9,4)]

a,b=map(int,input('두 정수를 입력하시오 :').split())

for i in range(0,5):
    if a+b == sum(mylist[i]): #합이 같으면 
        n,m=zip(*mylist)
        if a == n[i]: #첫 번째 숫자 비교
            print(f'{i+1}번째에 {mylist[i]} 요소가 있습니다.')
        elif b == n[i]: #두 번째 숫자 비교 
            print(f'{(a,b)} 요소는 없으나 {i+1}번째에 {mylist[i]} 요소가 있습니다.')

if (a, b) not in mylist and (b, a) not in mylist:
    print('이 요소는 없습니다.')
 
