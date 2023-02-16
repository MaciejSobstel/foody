import pandas as pd


def read_csv():
    df = pd.read_csv('db_utils/epi_r.csv')
    df = df[['title', 'calories', 'protein', 'fat', 'sodium', 'breakfast', 'dinner', 'lunch']]

    def meal_type(breakfast: bool, lunch: bool, dinner: bool):
        if breakfast:
            return 'breakfast'
        if dinner:
            return 'dinner'
        if lunch:
            return 'lunch'
        else:
            return 'UNK'

    df['meal_type'] = df.apply(lambda x: meal_type(x['breakfast'], x['lunch'], x['dinner']), axis=1)
    df = df[['title', 'calories', 'protein', 'fat', 'sodium', 'meal_type']]

    def replace(x):
        try:
            return x.replace("'", "")
        except:
            return x
    df = df.applymap(lambda x: replace(x))
    dict_list = df.to_dict(orient='records')
    return dict_list
