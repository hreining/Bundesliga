import pandas as pd
import src.preprocessing as pp


df = pd.read_csv('data/Bundesliga_Results.csv')

old_names=['FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']
new_names=['homegoals', 'awaygoals', 'winner', 'homehalf', 'awayhalf', 'winnerhalf']

df = pp.rename_cols(df, old_names, new_names)



print(df.head())