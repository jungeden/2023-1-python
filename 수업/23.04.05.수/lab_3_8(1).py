#1에서 100까지 합.
s=0
for i in range(0,101): #0부터 100까지 출력.
   s = s + i 

print('1에서 100까지의 합:',s)

#1에서 100까지의 짝수 합.
s = 0
for i in range(0,101,2): #0부터 100까지 짝수만 출력.
    s = s + i

print('1에서 100까지의 짝수의 합:',s)

#1에서 100까지의 홀수 합.
s = 0
for i in range(1,101,2): #1부터 100까지 홀수만 출력.
    s = s + i

print('1에서 100까지의 홀의 합:',s)
