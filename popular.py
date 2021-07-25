
from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
file = pd.read_csv('data/survey_results_public.csv')

filt = (file['Country'] == 'Bangladesh')
file.reset_index(inplace=True)

c = Counter()
file.dropna(axis='index', how='any', subset=['LanguageWorkedWith'], inplace=True)

for i in file.loc[filt]['LanguageWorkedWith']:
    c.update(i.split(';'))

languages = []
popularity = []

for cl in c.most_common(6):
    languages.append(cl[0])
    popularity.append(cl[1])

plt.pie(popularity, labels=languages, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("Popular language in bangladesh")
plt.tight_layout()
plt.show()
