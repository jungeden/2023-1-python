#ex4_25

s1 = 'Kang young min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

a=[s1,s2,s3,s4]
a2=[]
for i in range(4): 
    a_r = a[i].replace(' ','') #공백 삭제 
    a_r = a_r.replace('-','') #하이픈 삭제 
    a_r = a_r.upper() #대문자 
    a2.append(a_r)
    print(f'{a[i]}(은)는 {a_r}(으)로 수정됨')
for j in range(4):
    a_c = a2[j].count('N') #N 갯수 
    print(f'{a2[j]} : {a_c}개의 N이 나타남')

