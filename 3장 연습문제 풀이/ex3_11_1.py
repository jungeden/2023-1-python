#ex3_11

a,b,c=input('세 복권번호를 입력하시오 :').split()

a=int(a)
b=int(b)
c=int(c)


if (a==2 or a==3 or a==9) and (b==2 or b==3 or b==9) and (c==2 or c==3 or c==9):
    print('1억 원')
elif (a==2 or a==3 or a==9) or (b==2 or b==3 or b==9) or (c==2 or c==3 or c==9):
    if (a==2 or a==3 or a==9) and (b==2 or b==3 or b==9):
        print('1천만 원')
    else:
        if (a==2 or a==3 or a==9):
             print('1만 원')
        elif (b==2 or b==3 or b==9):
            print('1만 원')
        else:
            print('다음 기회에...')
    if (b==2 or b==3 or b==9) and (c==2 or c==3 or c==9):
        print('1천만 원')
    else:
        if (b==2 or b==3 or b==9):
             print('1만 원')
        elif (c==2 or c==3 or c==9):
            print('1만 원')
        else:
            print('다음 기회에...')    
else:
    print('다음 기회에...')
