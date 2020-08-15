def compare(AT,BT,month):
    A,B = AT[0],BT[0]
    if A[2] != B[2]:
        return A[2] < B[2]
    elif A[1] != B[1]:
        return A[1] < B[1]
    elif A[0]!=B[0]: 
        return A[0] < B[0]
    else:
        return int(AT[1]) < int(BT[1])

o = []
TP = {'E':1,'Q':3,'N':7,'F':14}
while True:
    month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    s = input().strip()
    if s == 'END':
        break
    ls = s.split()
    order,Type = ls[0],ls[1]
    d,m,y = int(ls[2]),int(ls[3]),int(ls[4])-543
    month[2] = 29 if (y%400==0) or (y%4==0 and y%100!=0) else 28
    if y+543 < 2558: 
        print('Error:',s,'-->','Invalid year')
        continue
    if not 1 <= m <= 12: 
        print('Error:',s,'-->','Invalid month')
        continue
    if not 1 <= d <= month[m]: 
        print('Error:',s,'-->','Invalid date')
        continue
    if Type not in ['E', 'Q', 'N', 'F']: 
        print('Error:',s,'-->','Invalid delivery type')
        continue
    
    d += TP[Type]
    if d > month[m]: 
        d %= month[m]
        m += 1
    if m > 12:
        m %= 12
        y += 1
    o.append(([d,m,y],order))

for i in range(len(o)):
    for j in range(len(o)):
        if compare(o[i],o[j],month):
            o[i],o[j] = o[j],o[i]
for item in o:
    date = item[0]
    print(str(item[1])+':','delivered on',str(date[0])+'/'+str(date[1])+'/'+str(date[2]+543))




