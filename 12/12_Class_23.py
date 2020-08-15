V = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
S = ['club','diamond','heart','spade']

class Card:
    def __init__(self, value="", suit=""):
        if suit: self.scr = V.index(value)*4 + S.index(suit)
        else: self.scr = value
    def __str__(self):
        inxV,inxS = self.scr//4,self.scr%4
        return '(' + V[inxV] + ' ' + S[inxS] + ')'
    def next1(self):
        return Card((self.scr+1)%52)
    def next2(self):
        self.scr = (self.scr+1)%52
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit)) 
for i in range(n):
    print(cards[i].next1()) 
print("----------")
for i in range(n):
    print(cards[i]) 
print("----------") 
for i in range(n):
    cards[i].next2() 
    cards[i].next2() 
    print(cards[i])

# 5
# A spade
# K heart
# K club
# 7 diamond
# 2 spade