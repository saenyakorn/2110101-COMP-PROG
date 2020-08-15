s = input()
sym = ['a','e','i','o','u']
if s[-1] == 'x' or s[-1] == 's' or s[-2:] == 'ch':
    print(s+'es')
elif s[-1] == 'y' and s[-2] not in sym:
    print(s[:-1]+'ies')
else:
    print(s+'s')