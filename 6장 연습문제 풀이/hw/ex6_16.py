#ex6_16
'''
student_tuple을 이용해 딕셔너리를 만들기
'''

student_tuple = ((191101, '홍길동', '010-123-45xx'), (191102, '임꺽정', '010-223-45xx'), (191103, '장길산', '010-323-45xx'))
a = (191101, '홍길동')
b = (191102, '임꺽정')
c = (191103, '장길산')
dictionary = dict((a, b, c))
print(f'학생 정보: {dictionary}')

n=int(input('학번을 입력하세요 : '))
while n != -1: #-1이 아닌 경우 
    if n in dictionary:
        print(f"{n}번 학생은 {dictionary[n]}입니다.")
    else:
        print("해당 학번의 학생이 없습니다.")
    n = int(input("학번을 입력하세요 :"))
        
print("프로그램을 종료합니다.")
