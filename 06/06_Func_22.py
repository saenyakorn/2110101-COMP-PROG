def distance1(x1, y1, x2, y2):
    return ((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2)**0.5
def distance2(p1, p2):
    return distance1(p1[0],p1[1],p2[0],p2[1])
def distance3(c1, c2):
    p1,p2 = [c1[0],c1[1]],[c2[0],c2[1]]
    return distance2(p1,p2),distance2(p1,p2) <= (float(c1[2])+float(c2[2]))
def perimeter(pl):
    point = [e for e in pl]
    l = 0
    for i in range(-1,len(point)-1):
        l += distance2(point[i],point[i+1])
    return l

if __name__ == "__main__":
    exec(input().strip())