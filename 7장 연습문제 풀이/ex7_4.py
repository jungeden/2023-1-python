#7_4
'''
난수 만들기
'''
#1
import random as rd

def my_rand():
    rand_num = rd.randint(0,1000000)
    print(rand_num)

for _ in range(10):
    my_rand()
print()

#2
import time

def my_rand():

    Time = int(time.time())
    random_seed = Time % 1000000

    for _ in range(5):
        random_seed = (random_seed * 32719 + 3) % 1000000
        randint = random_seed
        print(randint)

my_rand()

