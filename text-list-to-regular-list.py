s = input()

s_clean = s.replace("[", "").replace("]", "").replace("'", "")

L = s_clean.split(", ")
