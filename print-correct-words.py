words = input().split()

for word in words:
    if not word.startswith("*"):
        print(word)
