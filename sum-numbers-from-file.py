filename = input().strip()

with open(filename, "r") as f:
    numbers = f.readlines()

total = sum(int(x) for x in numbers)
print(total)
