# CSVReader
# CSVDictReader
# pandas

import pandas as pd

df = pd.read_csv('epi_r.csv')

df = df[['title', 'calories', 'protein', 'fat', 'sodium']]

dict_list = df[:10].to_dict(orient='records')

print(dict_list)