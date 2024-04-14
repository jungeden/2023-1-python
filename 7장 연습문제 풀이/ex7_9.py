#ex7_9
'''
random 모듈의 randrange()이용해 생성한 난수로 출력
'''
import random as rd

ro = rd.choice(['가위', '바위', '보'])
ju = rd.choice(['가위', '바위', '보'])

if ro == '가위' or ro == '바위' or ro == '보':
    if ju == ro:
       print('무승부')
   elif (ro == '가위' and ju =='바위') or (ro == '바위' and ju == '보') or (ro == '보' and ju == '가위'):
       print('로미오의 승부: {ro}')
       print('줄리엣의 승부: {ju}')
       print('로미오가 이겼습니다.')
   else:
       print('로미오의 승부: {ro}')
       print('줄리엣의 승부: {ju}')
       print('줄리엣이 이겼습니다.')

        

        

 

