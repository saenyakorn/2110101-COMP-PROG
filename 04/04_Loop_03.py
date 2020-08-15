def main():
    a = input()
    b = input()
    if len(a) != len(b):
        return print("Incomplete answer")
    t = 0
    for i in range(len(a)):
        t += (a[i]==b[i])
    return print(t)

if __name__=='__main__':
    main()