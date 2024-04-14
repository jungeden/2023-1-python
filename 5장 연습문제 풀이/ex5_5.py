#ex5_5
'''
list1과 list2를 조합
'''
list1 = ['I like','I love']
list2 = ['pancakes.','kiwi juice.','espresso.']

for i in range(0,2): #list1 반복 
    for j in range(0,3): #list2반복 
        print(f'{list1[i]} {list2[j]}')
