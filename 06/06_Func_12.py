def is_prime(n):
    n = int(n)
    if n <= 1:
        return 0
    for t in range(2,int(n**0.5)+1):
        if not n%t:
            return 0;
    return 1

def next_prime(n):
    n = int(n) + 1
    while True:
        if is_prime(n):
            print(n)
            exit()
        n += 1
        

def next_twin_prime(n):
    n = int(n) + 1
    while True:
        if is_prime(n) and is_prime(n+2):
            print("({}, {})".format(n,n+2))
            exit()
        n += 1

def main(): 
    exec(input().split()[0])

if __name__ == "__main__":
    main()