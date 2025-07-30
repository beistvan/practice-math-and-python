words = input().split("&")

seen = []
for w in words:
    if w not in seen:
        seen.append(w)

print(" ".join(seen))
