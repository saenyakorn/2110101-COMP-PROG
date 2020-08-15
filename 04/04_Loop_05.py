word,s = input(),input()
count = 0
a = ''
for i in range(len(s)):
    if ('A' <= s[i] and s[i] <= 'Z') or ('a' <= s[i] and s[i] <= 'z'): a += s[i]
    else : a += ' '
a = a.split()
for items in a :
    if word==items: count += 1
print(count)