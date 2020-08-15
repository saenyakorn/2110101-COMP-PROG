w = int(input())
print("{}".format("18" if w<=100 else ("22" if w<=250 else ("28" if w<=500 else ("38" if w<=1000 else ("58" if w<=2000 else "Reject"))))))