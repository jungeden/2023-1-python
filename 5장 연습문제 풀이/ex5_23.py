#ex5_23
'''
인물 정보를 리스트에 저장해 조건에 맞게 작성하기
'''
person1 =['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

#1
person_list=person1+person3+person4
def how_many_persons(lst): #사람수 
    return int(len(lst)/5)
               
n_persons=how_many_persons(person_list)
print(str(n_persons)+'명의 정보가 담겨있습니다.')

#2
person_list=person1+person2+person3+person4
def compute_average_age(person_list): #평균 나이 
    n=int(len(person_list)/5) 
    age=0
    for i in range(n):
        age += person_list[5*i + 1] 
    return age/n

average_age=compute_average_age(person_list)
print('평균 나이는'+str(average_age)+'세 입니다')

#3
person_list=person1+person2+person3+person4
def count_males_females(person_list): #성별 
    n=int(len(person_list)/5)
    cnt=0
    for i in range(n):
        cnt += person_list[5*i + 2] #남자
    return cnt,n-cnt #여자

n_male, n_female=count_males_females(person_list)
print('리스트에는 남자가 {}명, 여자가 {}명 입니다.'.format(n_male, n_female))

#4
person_list=person1+person2+person3+person4
def display_person(person_list) : #사람 나눠서 정렬
    Olist=[]
    mlist=[]
    for i in range(len(person_list)):
        mlist.append(person_list[i])
        if (i+1)%5 == 0: 
             Olist.append(mlist)
             mlist=[]
    return Olist

print (display_person(person_list))
