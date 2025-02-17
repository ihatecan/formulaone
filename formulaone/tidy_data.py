import json
import pandas as pd

from helpers import get_raw_data_path, get_tidy_data_path

tidy_data_path = get_tidy_data_path()
tidy_data_path.mkdir(parents=True, exist_ok=True)

with open(get_raw_data_path() / 'current.json', 'r') as f:
    d = json.load(f)

df = pd.json_normalize(d['year']['2 Guns']['Races'][0]['Results'])

df.to_parquet(tidy_data_path / 'current_race.parquet')


movies.get_item(Key={'year': 2013, 'title': '2 Guns'})