#ex4_23

def area_and_circumference(r): #원 넓이 둘레 함수 
    print('넓이 : {}, 둘레 : {}'.format((r**2)*3.14,2*r*3.14))

r=int(input('반지름을 입력하시오 :'))
while r>0:
    area_and_circumference(r)
    break
else:
    print('프로그램을 종료합니다.')
