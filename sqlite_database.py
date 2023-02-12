import sqlite3
from sqlite3 import Error
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


def main():
    conn = None
    try:
        conn = sqlite3.connect('data.db')
    except Error as e:
        print(e)
    else:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dishes (name TEXT, calories FLOAT, protein FLOAT, fat FLOAT, sodium FLOAT)")
        conn.commit()
        dishes = read_csv()
        for item in dishes:
            cursor.execute(f"INSERT INTO dishes (name, calories, protein, fat, sodium) VALUES ('{item['title']}', '{item['calories']}', '{item['protein']}', '{item['fat']}', '{item['sodium']}')")
        conn.commit()
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    conn = main()
