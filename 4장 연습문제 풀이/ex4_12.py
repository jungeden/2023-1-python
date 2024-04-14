#ex4_12

def cal_area(width,height):
    return (width*height)*0.5   #삼각형의 면적 

width=int(input('밑변을 입력하시오 :'))
height=int(input('높이를 입력하시오 :'))

print('삼각형의 면적 : {}'.format(cal_area(width,height)))
