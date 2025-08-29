n = int(input())  

res = 0
for x in range(n + 1):
    if x % 5 == 0 and x % 3 != 0:
        res += x

print(res)
