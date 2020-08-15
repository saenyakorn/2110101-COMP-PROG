def check(row,col):
    not_row = not('A'<=row<='Z' or 'a'<=row<='z') or len(row)>1
    not_col = not col.isdigit()
    if col.isdigit(): 
        col = int(col)
        not_col = not(1<=col<=52)
    if not_row or not_col:
        print('Invalid {}{}{}'.format('row ' if not_row else '','and ' if not_row and not_col else '','column' if not_col else ''))
    else:
        row = ord(row)-ord('a'if 'a'<=row<='z' else 'A')
        print('Black' if row%2==col%2 else 'White')

inp = input().strip()
if len(inp)<=3:
    # first condition
    row,col = inp[0],inp[1:].strip()
    check(row,col)
else:
    inp = [e.strip() for e in inp.replace(',','=').split('=')]
    dic = {}
    dic[inp[0]],dic[inp[2]] = inp[1],inp[3]
    row,col = dic['row'],dic['col']
    check(row,col)