x = int(input())
print("{}\n{}".format("positive" if x>0 else ("negative" if x<0 else "zero"),"odd" if x%2 else "even"))