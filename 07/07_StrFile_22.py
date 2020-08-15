def remake(s):
    s = s.lower()
    new_s = []
    for c in s:
        new_s += [c] if "a"<=c<="z" or "0"<=c<="9" else ""
    return new_s
s1 = sorted(remake(input().strip()))
s2 = sorted(remake(input().strip()))
print("YES" if s1==s2 else "NO")
