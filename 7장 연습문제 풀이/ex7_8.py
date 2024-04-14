#ex7_8
'''
주사위 게임
'''
import random as rd

ro = rd.randrange(1, 7)
ju = rd.randrange(1, 7)
print(f'로미오의 주사위 숫자는 {ro} 입니다.')
print(f'줄리엣의 주사위 숫자는 {ju} 입니다.')
if ro > ju:
    print('로미오가 이겼습니다.')
elif ro < ju:
    print('줄리엣이 이겼습니다.')
else:
    print('비겼습니다.')

