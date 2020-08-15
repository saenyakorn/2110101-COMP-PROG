n = int(input())
p1 = 0
p2 = 0
complete = False
for i in range(3*n):
    cmd1,cmd2 = input().split()
    if (cmd1=='R' and cmd2=='S') or (cmd1=='S' and cmd2=='P') or (cmd1=='P' and cmd2=='R'):
        p1 += 1
    elif (cmd2=='R' and cmd1=='S') or (cmd2=='S' and cmd1=='P') or (cmd2=='P' and cmd1=='R'):
        p2 += 1
    if p1 >= n or p2 >= n:
        complete = True
        break

print(p1,p2)
print("{}".format("Tie" if not complete else ("Player 1 wins" if p1 > p2 else "Player 2 wins")))