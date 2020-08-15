import sys

def main():
    i = 0
    cmd = ''
    mx1 = mx2 = -sys.maxsize
    mn1 = mn2 = sys.maxsize
    while True:
        cmd = input()
        if cmd == "Zig-Zag" or cmd == "Zag-Zig":
            return print(mn1 if cmd=="Zig-Zag" else mn2,mx1 if cmd=="Zig-Zag" else mx2)
        x,y = cmd.split()
        L = (int(x),int(y))
        mn1 = min(mn1,L[i%2])
        mn2 = min(mn2,L[(i+1)%2])
        mx1 = max(mx1,L[(i+1)%2])
        mx2 = max(mx2,L[i%2])
        i += 1

if __name__=='__main__':
    main()