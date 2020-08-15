def union(ls,st):
    for i in range(len(ls)):
        st.add(ls[i])
    return st
def intersect(ls,st):
    ch = set()
    for i in range(len(ls)):
        if ls[i] in st: ch.add(ls[i])
    return ch

n = int(input())
un,it = set(),set();
for i in range(n):
    ls = [int(e) for e in input().split()]
    if i==0:
        for j in range(len(ls)):
            it.add(ls[j])
    un = union(ls,un)
    it = intersect(ls,it)
print(len(un))
print(len(it))


# 3 
# 1 2 1 2 3 1 2 1 2 1
# 2 3
# 2 5 4 3

# 6
# 100 1000 
# 101 123 
# 200
# 201
# -1
# -2 -3