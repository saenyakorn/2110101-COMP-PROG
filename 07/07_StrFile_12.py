s = input()
new_s = ""
for c in s:
    new_s += c if "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9" else " "
x = new_s.split()
s = ""
for i in range(0,len(x)):
    x[i] = x[i].lower()
    if i>0 : x[i] = x[i][0].upper() + x[i][1:]
    s += x[i]
print(s)