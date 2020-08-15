score = float(input())
print("{}".format("A" if score>=80 else ("B" if score>=70 else ("C" if score>=60 else ("D" if score>=50 else "F")))  ))