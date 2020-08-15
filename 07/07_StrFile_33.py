fname1,fname2 = [e for e in input().strip().split()]
f1,f2 = open(fname1,"r"),open(fname2,"r")
dat1,dat2 = f1.read().split(),f2.read().split()
i,j = 0,0

while i <len(dat1) and j < len(dat2):
    if int(dat1[i][-2:]) < int(dat2[j][-2:]):
        print(dat1[i],dat1[i+1])
        i += 2
    elif int(dat1[i][-2:]) > int(dat2[j][-2:]):
        print(dat2[j],dat2[j+1])
        j += 2
    else:
        if int(dat1[i][:2]) < int(dat2[j][:2]):
            print(dat1[i],dat1[i+1])
            i += 2
        elif int(dat1[i][:2]) > int(dat2[j][:2]):
            print(dat2[j],dat2[j+1])
            j += 2
        else :
            if float(dat1[i+1]) < float(dat2[j+1]):
                print(dat1[i],dat1[i+1])
                i += 2
            else :
                print(dat2[j],dat2[j+1])
                j += 2
while i <len(dat1):
    print(dat1[i],dat1[i+1])
    i += 2
while j < len(dat2):
    print(dat2[j],dat2[j+1])
    j += 2