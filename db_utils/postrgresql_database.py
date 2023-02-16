import psycopg2
from psycopg2 import OperationalError

from read_csv import read_csv


def main():
    conn = None
    try:
        conn = psycopg2.connect(
            database="foody",
            user="postgres",
            password="postgres",
            host="localhost")
    except OperationalError as e:
        print(e)
    else:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dishes (name TEXT, calories FLOAT, protein FLOAT, fat FLOAT, sodium FLOAT)")
        cursor.execute("ALTER TABLE dishes ADD COLUMN meal_type TEXT")
        conn.commit()
        dishes = read_csv()
        for item in dishes:
            cursor.execute("UPDATE dishes SET meal_type = %s WHERE name = %s", (item['meal_type'], item['title']))
        conn.commit()
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    conn = main()
