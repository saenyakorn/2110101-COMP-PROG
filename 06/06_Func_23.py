def make_int_list(x):
    return [int(e) for e in x.split()]
def is_odd(e):
    return True if e%2 else False
def odd_list(alist):
    ls = []
    for x in alist:
        x%2 and ls.append(x)
    return ls
def sum_square(alist):
    sm = 0
    for x in alist:
        sm += x*x
    return sm

if __name__ == "__main__":
    exec(input().strip())