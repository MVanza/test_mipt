import pandas as pd
from collections import Counter

df1 = pd.read_csv('games001.csv', delimiter=';')
df2 = pd.read_csv('rates001.csv', delimiter=';')
d = df2.merge(df1, on='id')
lst = []
company_name = []
for i in range(1, len(d['id'].unique())+1):
    m = d.loc[d['id'] == i, 'mark'].mean()
    lst.append([m, d.loc[d['id'] == i, 'name'].unique()[0]])
    if m > 8:
        company_name.append(d.loc[d['id'] == i, 'company'].unique()[0])
c = Counter(company_name)
lst.sort()
print(lst[-1][1], f'{lst[-1][0]:.3f}')
print(lst[-2][1], f'{lst[-2][0]:.3f}')
print(lst[-3][1], f'{lst[-3][0]:.3f}')
print(c.most_common(1)[0][0], c.most_common(1)[0][1])
