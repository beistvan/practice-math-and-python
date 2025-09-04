n = int(input())

def donuts(n):
    if n > 9:
        return "Number of donuts: a lot"
    else:
        return f"Number of donuts: {n}"

print(donuts(n))

