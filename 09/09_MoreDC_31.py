def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def is_coprime(a,b,c):
    return bool(gcd(gcd(a,b),c)==1)

def primitive_Pythagorean_triples(max_len):
    triple = []
    for i in range(max_len):
        for j in range(i+1,max_len):
            for k in range(j+1,max_len):
                if k*k == i*i + j*j and is_coprime(i,j,k): triple += [[i,j,k]]
    triple.sort(key=lambda x:x[2])
    return triple

if __name__ == "__main__":
    exec(input().strip())

# print(is_coprime(2,3,6),is_coprime(2,4,8))
# print(primitive_Pythagorean_triples(10))
# print(primitive_Pythagorean_triples(20))