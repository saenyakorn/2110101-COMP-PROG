x = input()
l = len(x) if len(x)!=4 and len(x)!=7 and len(x)!= 10 else len(x)+1
if len(x)<=3 :
    print(x)
elif len(x)<=6 :
    print( x[:l-4] + "{}{}K".format("." if len(x)==4 else "", int(x[l-4])+1 if int(x[l-3])>=5 else int(x[l-4])) )
elif len(x)<=9 :
    print( x[:l-7] + "{}{}M".format("." if len(x)==7 else "", int(x[l-7])+1 if int(x[l-6])>=5 else int(x[l-7])) )
else :
    print( x[:l-10] + "{}{}B".format("." if len(x)==10 else "", int(x[l-10])+1 if int(x[l-9])>=5 else int(x[l-10])) )