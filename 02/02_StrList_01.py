n = input()
x = 0
for i in range(12) :
    x += (13-i) * int(n[i])
n += str((11-x%11)%10)
print(n[0],n[1:5],n[5:10],n[10:12],n[12])

#n12 = (11 – (13n0+12n1+11n2+10n3+9n4+8n5+7n6+6n7+5n8+4n9+3n10+2n11) mod 11) mod 10