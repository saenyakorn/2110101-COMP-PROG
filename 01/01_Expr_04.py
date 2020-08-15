import math

W = float(input())
H = float(input())

a = math.sqrt(W*H)/60
b = 0.024265 * (W**0.5378) * (H**0.3964)
c = 0.0333 * (W**(0.6157-0.0188*math.log10(W))) * (H**0.3)

print(a)
print(b)
print(c)
