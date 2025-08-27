import os

path = input().strip()

if not os.path.exists(path):
    print("ERROR:")
    print("File not exist")
elif os.path.isdir(path):
    print("ERROR:")
    print("It's a directory, not a file")
else:
    print("CONTENT:")
    with open(path, "r", encoding="utf-8") as f:
        print(f.read(), end="")
