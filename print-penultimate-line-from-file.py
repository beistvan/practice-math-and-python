filename = input().strip()

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]

print(lines[-2])
