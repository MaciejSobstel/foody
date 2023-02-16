import sqlite3
from sqlite3 import Error

from db_utils.read_csv import read_csv


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
