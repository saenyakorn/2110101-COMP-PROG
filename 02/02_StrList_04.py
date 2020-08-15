m = input()
n = int(input())
output = ("0" * (n-len(m)) + m) if (len(m) < n) else (m)
print(output)