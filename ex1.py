import numpy as np


N, M = tuple(map(int, input().split()))
c = np.zeros(N, M)

for i in range(N):
    c[i] += (list(map(int, input().split())))
S = 0
V = 0

for i in range(N):
    for j in c[i]:
        if j < 0:
            V += j
            if j < -5:
                S += 1

print(S)
print(abs(int(V)))
print(int(c.max()))
