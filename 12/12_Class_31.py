class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1 
        self.upperright = p2
    def area(self): 
        x1,y1,x2,y2 = self.lowerleft.x, self.lowerleft.y, self.upperright.x, self.upperright.y
        return (x2-x1)*(y2-y1)
    def contains(self, p):
        x1,y1,x2,y2 = self.lowerleft.x, self.lowerleft.y, self.upperright.x, self.upperright.y
        if x1 <= p.x <= x2 and y1 <= p.y <= y2: 
            return True
        else: 
            return False

x1,y1,x2,y2 = [int(e) for e in input().split()] 
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright) 
print(rect.area())
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()] 
    p = Point(x,y)
    print(rect.contains(p))

# 2 2 10 10 
# 4
# 0 0
# 2 4
# 3 5 
# 10 1