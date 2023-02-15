import pandas as pd


def read_csv():
    df = pd.read_csv('epi_r.csv')
    df = df[['title', 'calories', 'protein', 'fat', 'sodium']]

    def replace(x):
        try:
            return x.replace("'", "")
        except:
            return x
    df = df.applymap(lambda x: replace(x))
    dict_list = df.to_dict(orient='records')
    return dict_list
