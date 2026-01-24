import numpy as np

data1 = list(map(int, input().split(',')))
data2 = list(map(int, input().split(',')))

V1 = np.array(data1)
V2 = np.array(data2)

divisor = V2[-2]

V = V1[V1 % divisor == 0] / divisor

