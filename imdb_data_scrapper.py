import pandas as pd


imdb_akas_df = pd.read_csv('title.akas.tsv/data.tsv', sep='\t', low_memoryh=False)
print(imdb_akas_df.head())
print(imdb_akas_df.shape)