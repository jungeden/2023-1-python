with open('number1to10.txt','r') as f:
    numbers=[int(line.strip())*10 for line in f]
with open('numberby10.txt','w') as f:
    for number in numbers:
        f.write(str(number)+'\n')
