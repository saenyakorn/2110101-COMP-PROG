fileName = input().strip()
f = open(fileName,'r')
n = int(input())
for i in range(1,n//10+1):
    print('-'*(10-len(str(i))) + str(i),end="")
print('-'*(n%10))

inp = ""
for line in f:
    inp += line.strip('\n').strip() + '.'
inp.strip('.')

i = 0
o = ""
ls = []
while i < len(inp):
    j,word = i,""
    while j < len(inp) and inp[j]!='.':
        word += inp[j]
        j += 1
    if inp[i]=='.':
        o += '.'
        i += 1
    elif len(o)+len(word) <= n:
        o += word
        i = j
    else:
        ls += [o.strip('.')]
        o = word
        i = j
ls += [o.strip('.')]
for w in ls:
    if w.strip('.')!='': print(w.strip('.'))