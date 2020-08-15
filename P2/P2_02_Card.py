num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
gp = ['C','D','H','S']
s = input().strip()
o = ''
for i in range(0,len(s)-2,2):
    f1,f2 = num.index(s[i]) + 1,num.index(s[i+2]) + 1
    b1,b2 = gp.index(s[i+1]) + 1,gp.index(s[i+3]) + 1
    cont = f1-f2
    if cont == 0:
        cont = b1-b2
    o += str(cont) if cont <= 0 else '+' + str(cont)
print(o)