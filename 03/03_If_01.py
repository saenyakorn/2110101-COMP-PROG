L = ["01","02"]
for i in range(20,41) :
    L += [str(i)]
L += ["51","53","55","58"]
x = str(input())
print("{}".format("OK" if x in L else "Error"))