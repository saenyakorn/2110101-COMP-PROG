import math

menu = {'P01':265.3, 'P02':246.9, 'P03':256.9, 'P04':272.5, 'P05':309.3}
customer = {}
for i in range(int(input().split(':')[1])):
    userid = input().split(':')[1].strip()
    cmd = input().split(',')
    user = cmd[0]
    cal = 0
    for i in range(1,len(cmd),2):
        m,n = cmd[i],int(cmd[i+1])
        cal += menu[m]*n
    if user in customer: customer[user][0] += cal
    else: customer[user] = [cal,i]

out = []
for k,v in customer.items():
    out += [(k,math.ceil(v[0]),v[1])]

print("Before ascedning sort")
exp = [(a,b) for a,b,c in sorted(out,key=lambda x:x[2])]
print(exp)
print("After ascedning sort")
exp = [(a,b) for a,b,c in sorted(sorted(out,key=lambda x:x[0]),key=lambda x:x[1])]
print(exp)
    
# Number of customer: 3 
# Customer: 1 
# Kevin,P05,3 
# Customer: 2 
# Smith,P05,2 
# Customer: 3 
# Jordan,P01,4

# Number of customer: 6
# Customer: 1 
# Aa,P01,2,P03,2 
# Customer: 2 
# Ab,P04,3,P03,1 
# Customer: 3 
# Ac,P01,2,P03,2 
# Customer: 4 
# Ad,P05,4,P03,1 
# Customer: 5 
# Ae,P03,1,P05,1
# Customer: 6
# Ae,P03,10,P01,3