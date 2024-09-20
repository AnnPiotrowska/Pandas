
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

# Przegląd danych

print(df.columns)
print(df.head())

# Ile państw wyszczególniono dla każdego kontynentu?

print(df.groupby('continent')['country'].nunique())

# Jaka była średnia długość życia dla każdego roku ujętego w naszych danych?

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

# Jakie są średnia długość życia i produkt krajowy brutto (GDP)? Dane podzielone według kontynentów

multi_group_var = df.groupby(['continent', 'year'])[['lifeExp','gdpPercap']].mean()
print(multi_group_var)

# Wykres prezentujący średnią długość życia w skali czasu

global_yearly_life_expectancy.plot()
plt.show()






