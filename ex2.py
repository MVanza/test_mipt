import numpy as np

with open(input()) as f:
    n1 = np.array(list(map(float, f.read().split())))

with open(input()) as f:
    n2 = np.array(list(map(float, f.read().split())))

n3 = np.array(list(map(float, input().split())))
n1 = np.reshape(n1, (len(n2), len(n3)))

A2 = np.linalg.matrix_power(n1, 2)

print(A2.dot(n3).dot(n2))
