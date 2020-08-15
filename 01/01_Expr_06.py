h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

s3 = s2-s1
if s3 < 0 :
    s3 += 60
    m2 -= 1

m3 = m2-m1
if m3 < 0 :
    m3 += 60    
    h2 -= 1

h3 = h2-h1
if h3 < 0 :
    h3 += 24

print(h3,m3,s3,sep=':')