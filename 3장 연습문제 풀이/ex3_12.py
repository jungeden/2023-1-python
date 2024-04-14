#ex3_12
r=5
x,y=map(int,input('점의 좌표 x,y를 입력하시오 :').split())

if (x*x+y*y)**0.5 > r: #점과 원점 사이 거리가 반지름보다 큰 경우 
    print('원의 외부에 있음')
else:
    print('원의 내부에 있음')
