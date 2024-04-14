#ex3_25
height = 0
day = 0

while height<=30: #높이가 30미터 될 때 까지 반복  
    day=day+1
    height=7+7*(day-1)-5*(day-1) #첫째날 7미터 더하기

    print('day :{} 달팽이의 위치 : {}미터'.format(day,height))            
    
print()
print('우물을 탈출하는 데 걸린 날은 {}일 입니다.'.format(day))


