import numpy as np

a = np.linalg.norm(A2 - A3)
b = np.linalg.norm(A1 - A3)
c = np.linalg.norm(A1 - A2)

p = (a + b + c) / 2

S = np.sqrt(max(p * (p - a) * (p - b) * (p - c), 0))

print(S)
