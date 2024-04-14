#ex6_3
'''
커피 가게의 메뉴와 가격을 딕셔너리로 작성하기
'''

#1
menu = {'Americano':'3,000원','Ice Americano':'3,500원','Cappuccino':'4,000원','Caffe Latte':'4,500원','Espresso':'3,600원'}

for key in menu: #메뉴
    print(f'{key:13s} 가격 : {menu[key]}')

#2
m=input('위의 메뉴중 하나를 선택하세요 :')
if m in menu: #메뉴에 있으면 
    print(f'{m}는 {menu[m]} 입니다. 결제를 부탁합니다.')
else : #없으면 
    print(f'미안합니다. {m}는 메뉴에 없습니다.')
    
