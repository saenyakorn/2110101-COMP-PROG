dic = {}
for i in range(int(input().strip())):
    mov,n1,n2 = [e.strip() for e in input().split(',')]
    if n1 in dic: dic[n1] += [mov]
    else: dic[n1] = [mov]
    if n2 in dic: dic[n2] += [mov]
    else: dic[n2] = [mov]

lsname = [e.strip() for e in input().split(',')]
for name in lsname:
    if name in dic:
        print("{} -> {}".format(name,', '.join(dic[name])))
    else:
        print("{} -> Not found".format(name))

# 9
# Rush Hour, Jackie Chan, Chris Tucker
# Shanghai Noon, Jackie Chan, Owen Wilson
# Shanghai Knights, Jackie Chan, Owen Wilson
# The Medallion, Jackie Chan, Lee Evans
# Wedding Crashers, Owen Wilson, Vince Vaughn
# Midnight in Paris, Owen Wilson, Rachel McAdams
# Mousehunt, Nathan Lane, Lee Evans
# The Forbidden Kingdom, Jackie Chan, Jet Li
# The One, Jet Li, Jason Statham
# Jet Li, Lee Evans, Tony Jaa