n = input()
a = b = ""
for i in range(3,len(n),7) :
    a += n[i]
for i in range(7,len(n),5) : 
    b += n[i]
c = str(int(a) + int(b) + 10000)
d = (int(c[-2])+int(c[-3])+int(c[-4]))%10 + 1
print(c[-4:-1] + chr(d+ord('A')-1))