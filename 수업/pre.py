def A(n):
    ap=['1','2','3','4','5','6','7','8','9','0']
    for i in n:
        list(str(i))
        aa=i[0]
        if aa in ap:
            i=int(i)
            n.append(i)
n=['12','apple','24']
A(n)
print(n)
