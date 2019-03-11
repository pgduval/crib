import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
sns.set(style="whitegrid")
PATH = '/home/elmaster/project/crib'
data = pd.read_csv(os.path.join(PATH, 'scoring.csv'))

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', 100)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199


data.sort_values(by='score', ascending=False, inplace=True)


print(data.query('score == 19'))
print(data.head())
grouped = data.groupby('score').count().reset_index()
grouped['norm_count'] = grouped['hand'] / sum(grouped['hand'])
print(grouped.head(20))


grouped = data.groupby('hand').count().reset_index()
print(grouped)


plt.bar(grouped['score'], grouped['norm_count'])
plt.show()

print(grouped.columns)
sns.barplot(x="score", y="norm_count", data=grouped,
            label="Alcohol-involved", color="b")
plt.show()

print(len(data))
print(sum(grouped['hand']))

print(grouped['hand'])

for i in grouped['hand'].values:
    print(i)


print(data.query('score == 28'))    