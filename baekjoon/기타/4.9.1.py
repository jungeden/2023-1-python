import turtle

# 함수 정의: 좌표가 사각형 내부에 있는지 판별
def is_inside(x1, y1, x2, y2, px, py):
    return x1 < px < x2 and y1 < py < y2

# 좌표 입력 받기
x1 = int(turtle.textinput("좌표 입력", "왼쪽 하단 모서리 좌표 (x1, y1):").strip())
y1 = int(turtle.textinput("", "").strip())
x2 = int(turtle.textinput("", "오른쪽 상단 모서리 좌표 (x2, y2):").strip())
y2 = int(turtle.textinput("", "").strip())

# 점의 좌표 입력 받기
px = int(turtle.textinput("테스트 점 입력", "x 좌표:").strip())
py = int(turtle.textinput("", "y 좌표:").strip())

# turtle 그래픽 창 초기화
turtle.speed(0)
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y1)
turtle.goto(x2, y2)
turtle.goto(x1, y2)
turtle.goto(x1, y1)

# 점 그리기
turtle.penup()
turtle.goto(px, py)
turtle.pendown()
turtle.dot(5, 'red')

# 판별 및 결과 출력
if is_inside(x1, y1, x2, y2, px, py):
    turtle.write("점은 사각형의 내부에 있습니다", font=("Arial", 12, "normal"))
else:
    turtle.write("점은 사각형의 외부에 있습니다", font=("Arial", 12, "normal"))

# 화면 유지
turtle.done()
