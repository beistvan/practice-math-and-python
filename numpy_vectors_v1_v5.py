import numpy as np

data = list(map(float, input().split(',')))


V1 = np.array(data)
V2 = V1[-2:-1]
V3 = V1[::-1]
V4 = V1[::3]
V5 = np.arange(len(V1))

