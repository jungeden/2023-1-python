#ex4_26

s1 = 'Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho (Bython city), Koo(C city), Ryu(C++ city)'
print(f'주어진 문자열 :\n {s1}')
print()
print(f'수정된 문자열 :\n {s1.replace("Bython","Python")}') #수정 
print(f'Bython 문자열은 모두 {s1.count("Bython")}번 수정했습니다.') #횟수 
