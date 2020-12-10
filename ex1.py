import numpy as np
import pandas as pd

N, M = tuple(map(int, input().split()))
df = pd.DataFrame()
for i in range(N):
    d = np.array(list(map(int, input().split())))
    df[f'string{i}'] = d.transpose()
# 1
S = 0
V = 0
maximum = 0
for i in range(N):
    # 1
    ds = df[df[f'string{i}'] < -5]
    S += len(ds.loc[:, f'string{i}'].values)
    # 2
    dv = df[df[f'string{i}'] < 0]
    V += sum(dv.loc[:, f'string{i}'].values)

# 3
m = df.max().values
print(S)
print(abs(V))
print(max(m))
