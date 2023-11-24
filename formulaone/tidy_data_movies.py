import json
import pandas as pd

from helpers import get_path_to_data, get_tidy_data_path

tidy_data_path = get_tidy_data_path()
tidy_data_path.mkdir(parents=True, exist_ok=True)

with open(get_path_to_data() / 'RawData/rawdata.json', 'r') as f:
    d = json.load(f)

# Konvertieren Sie die "Items" Liste in einen DataFrame
df = pd.DataFrame(d["Items"])

# Optional: Expandieren Sie die Spalten im "info"-Dictionary
info_df = pd.json_normalize(df['info'])
df = pd.concat([df, info_df], axis=1).drop('info', axis=1)

df.reset_index(inplace=True)
df.rename(columns={'index': 'ID'}, inplace=True)

# print(df)

# Expandieren der "actors"-Spalte
df_actors = df[['ID', 'title', 'actors']].explode('actors')
df_actors.columns = ['ID_movie', 'title', 'actor']
df_actors.to_csv(tidy_data_path / 'actors.csv')

# print(df_actors.head())

# Expandieren der "genres"-Spalte
df_genres = df[['ID', 'title', 'genres']].explode('genres')
df_genres.columns = ['ID_movie', 'title', 'genre']
df_genres.to_csv(tidy_data_path / 'genres.csv')

# print(df_genres.head())

# Expandieren der "directors"-Spalte
df_directors = df[['ID', 'title', 'directors']].explode('directors')
df_directors.columns = ['ID_movie', 'title', 'director']
df_directors.to_csv(tidy_data_path / 'directors.csv')

# print(df_directors.head())

# das Erscheinungsdatum in Tag, Monat und Jahr aufteilen
df['release_year'] = pd.to_datetime(df['release_date']).dt.year
df['release_month'] = pd.to_datetime(df['release_date']).dt.month
df['release_day'] = pd.to_datetime(df['release_date']).dt.day

# Expandierte Spalten, release_date und year aus dem DataFrame entfernen
columns_to_remove = ['actors', 'genres', 'directors', 'release_date', 'year']
df = df.drop(columns=columns_to_remove)

# df.to_parquet(tidy_data_path / 'tidydata.parquet')
df.to_csv(tidy_data_path / 'tidydata.csv')
