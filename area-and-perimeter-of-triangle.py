a = float(input())
b = float(input())
c = float(input())

P = a + b + c
print(P)

s = P / 2

S = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(S)
