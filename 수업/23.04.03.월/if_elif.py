s = int(input('점수를 입력하세요 :'))
if s >= 90:
    grade = 'A' # 90 이상인 경우 A.
elif s >= 80:
    grade ='B' # A가 아닌경우, 80 이상이면 B.
elif s >= 70:
    grade ='C' # B도 아닌경우, 70 이상이면 C.
elif s >= 60:
    grade ='D' # C도 아닌 경우, 60 이상이면 D.
else:
    grade = 'F' # 그 외의 경우 F.

print('당신의 등급은 :', grade)    
