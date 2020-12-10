import numpy as np
import pandas as pd

N, M = tuple(map(int, input().split()))
df = pd.DataFrame()
for i in range(N):
    d = np.array(list(map(int, input().split())))
    df[f'string{i}'] = d.transpose()
summ = 0
for i in range(N):
    d = df[df[f'string{i}'] < -5]
    d1 = d.loc[:, f'string{i}'].values
    summ += len(d1)

print(summ)
