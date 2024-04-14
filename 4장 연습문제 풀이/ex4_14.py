#ex4_14

def sort3(num1,num2,num3): #세 수 정렬 함수 
    a=[]
    a.append(num1)
    a.append(num2)
    a.append(num3)
    a.sort()
    print('정렬된 리스트는 다음과 같습니다 : {} {} {}'.format(a[0],a[1],a[2]))

n1 = int(input('세 수를 입력하세요 :\n'))
n2 = int(input())
n3 = int(input())
sort3(n1,n2,n3)


