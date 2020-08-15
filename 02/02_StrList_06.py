a = input()
b = input()
num_a = list(map(float,a[1:-1].split(', ')))
num_b = list(map(float,b[1:-1].split(', ')))
a = b = c = "["
for i in range(len(num_a)) :
    a += str(num_a[i]) + (", " if len(num_a)-1 > i else "]")
    b += str(num_b[i]) + (", " if len(num_a)-1 > i else "]")
    c += str(num_a[i]+num_b[i]) + (", " if len(num_a)-1 > i else "]")
print("{} + {} = {}".format(a,b,c))
