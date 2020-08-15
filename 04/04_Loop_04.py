s = str(input())
a = str()
for i in range(len(s)):
    a += '[' if s[i]=='(' else ('(' if s[i]=='[' else (')' if s[i]==']' else (']' if s[i]==')' else s[i])))
print(a)