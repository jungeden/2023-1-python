s= int(input('자동차의 속도를 입력하세요(단위 : km/h) :'))
if s >= 100:
    g ='고속'
elif 60 <= s < 100:
    g = '중속'
else: 
    g = '저속'

print(g)    
