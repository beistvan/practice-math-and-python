import math

a = float(input())

S = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * a**2
V = (1/4) * (15 + 7 * math.sqrt(5)) * a**3

print(round(S, 2))
print(round(V, 2))
