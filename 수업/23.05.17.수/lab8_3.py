a=[1,2,3,4,5]
print(f'a = {a}')
try:
    b = input('a의 요소를 하나 선택하시오 :')
    i = a.index(int(b))
except:
    print('입력 값이 정수나 실수가 아님')
else:
    if i == 0:
        print(f'{b}은(는) 첫번째 요소입니다.')
    elif i == 1:
         print(f'{b}은(는) 두번째 요소입니다.')
    elif i == 2:
         print(f'{b}은(는) 세번째 요소입니다.')
    elif i == 3:
         print(f'{b}은(는) 네번째 요소입니다.')
    elif i == 4:
         print(f'{b}은(는) 다섯번째 요소입니다.')
    elif i == 5:
         print(f'{b}은(는) 여섯번째 요소입니다.')
   
