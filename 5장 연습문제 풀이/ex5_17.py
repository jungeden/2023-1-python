#ex5_17
'''
animals 리스트 만들고 조건에 따라 출력
'''
#1
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals = {}'.format(animals))

#2
animals.append(animals.pop(0))
print('animals = {}'.format(animals))

#3
animals = ['dog', 'cat', 'tiger', 'lion']
print('animals = {}'.format(animals))
for i in animals:
    print('I love {}.'.format(i))
