class Complex :
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        a,b = self.a,self.b
        s = ""
        if b == 1: s = '+i'
        elif b == -1: s = '-i'
        elif b > 0: s = '+'+str(b)+'i'
        elif b < 0: s = str(b)+'i'
        return "0" if a==0 and b==0 else ("{}{}".format(a if a!=0 else "",s if a!=0 else ("" if s=="" else (s[1:] if s[0]=='+' else s))))
    def __add__(self, rhs):
        return Complex(self.a+rhs.a,self.b+rhs.b)
    def __mul__(self, rhs):
        a,b,c,d = self.a,self.b,rhs.a,rhs.b
        return Complex(a*c - b*d,a*d + b*c)
    def __truediv__(self, rhs):
        a,b,c,d = self.a,self.b,rhs.a,rhs.b
        return Complex((a*c + b*d)/(c*c + d*d),(-a*d + b*c)/(c*c + d*d))

def abs(x):
    return x if x>0 else -x

t, a, b, c, d = [int(x) for x in input().split()] 
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else        : print(c1/c2)