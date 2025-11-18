import numpy as np

data1 = list(map(int, input().split(',')))
data2 = list(map(int, input().split(',')))

V1 = np.array(data1)
V2 = np.array(data2)
V3 = V1 + V2

V4 = V1[::2] * V2[::-1][::2]
