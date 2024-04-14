#ex3_19_1

print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('- 햄버거(입력 b)\n- 치킨(입력 c)\n- 피자(입력 p)')

selected=input('메뉴를 선택하세요(알파벳 b,c,p 입력) :')
b='햄버거'
c='치킨'
p='피자'

if selected == 'b':
    print(b,'을(를) 선택하였습니다.')
elif selected == 'c':
    print(c,'을(를) 선택하였습니다.')
elif selected == 'p':
    print(p,'을(를) 선택하였습니다.')
    
selected = None
while selected not in ['b', 'c', 'p']:
    selected = input('메뉴를 다시 입력하세요(알파벳 b,c,p 입력) :')

if selected==b:
    print(b,'을(를) 선택하였습니다.')
elif selected==c:
    print(c,'을(를) 선택하였습니다.')
else:
    print(p,'을(를) 선택하였습니다.')
