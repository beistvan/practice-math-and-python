s = input()

def fix_start(s):
    if not s:
        return ""
    first = s[0]
    return first + s[1:].replace(first, "*")

print(fix_start(s))

