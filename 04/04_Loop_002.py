d = list(int(e) for e in input().split())
p,i,j = d[-1],-1,0
while j < len(d)-1 :
    if d[j] <= p :
        i += 1
        d[i],d[j] = d[j],d[i]
    j += 1
d[i+1],d[-1] = d[-1],d[i+1]
print(d)