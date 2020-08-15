V = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10}
S = {'club':1,'diamond':2,'heart':3,'spade':4}
T = ['3','4','5','6','7','8','9','J','Q','K','A','2']

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'
    def getScore(self):
        return V[self.value]
    def sum(self, other):
        return (V[self.value]+V[other.value])%10
    def __lt__(self, rhs):
        if self.value == rhs.value:
            return S[self.suit] < S[rhs.suit]
        else:
            return T.index(self.value) < T.index(rhs.value)

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit)) 
for i in range(n):
    print(cards[i].getScore()) 
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1])) 
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])