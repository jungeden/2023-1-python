import random
r_n=[random.randint(1,10) for i in range(30)]
with open('randint30.txt','w') as f:
    for num in r_n:
        f.write(str(num) + ' ')
        
with open('randint30.txt','r') as f:
    a=f.read()
    for j in range(10):
        b=a.count(str(j))
        print(f'{j+1} : {b}개')
