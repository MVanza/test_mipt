import numpy as np
import pandas as pd

df1 = pd.read_csv('games001.csv', delimiter=';')
df2 = pd.read_csv('rates001.csv', delimiter=';')
d = df2.merge(df1, on='id')
lst = []
for i in range(1, len(d['id'].unique())+1):
    m = d.loc[d['id'] == i, 'mark'].mean()
    lst.append([m, d.loc[d['id'] == i, 'name'].unique()[0]])

print(sorted(lst)[-1][1], f'{sorted(lst)[-1][0]:.3f}')
print(sorted(lst)[-2][1], f'{sorted(lst)[-2][0]:.3f}')
print(sorted(lst)[-3][1], f'{sorted(lst)[-3][0]:.3f}')
