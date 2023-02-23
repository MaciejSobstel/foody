import argparse
from dotenv import dotenv_values
from pathlib import Path
import psycopg2
from psycopg2 import OperationalError

from read_csv import read_csv

config = dotenv_values() 


def migrate(csv_path: Path):
    try:
        conn = psycopg2.connect(
            database=config["DB_NAME"],
            user=config["DB_USER"],
            password=config["DB_PASSWORD"],
            host=config["DB_HOST"],
            port=config["DB_PORT"])
    except OperationalError as e:
        print(e)
    else:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dishes (name TEXT, calories FLOAT, protein FLOAT, fat FLOAT, sodium FLOAT, meal_type TEXT)")
        conn.commit()
        dishes = read_csv(csv_path)
        for item in dishes:
            cursor.execute(f"INSERT INTO dishes (name, calories, protein, fat, sodium, meal_type) VALUES ('{item['title']}', '{item['calories']}', '{item['protein']}', '{item['fat']}', '{item['sodium']}', '{item['meal_type']}')")
        conn.commit()
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Migrate csv to postgresql")
    parser.add_argument("--csv_path", type=Path, required=True)
    args = parser.parse_args()

    migrate(args.csv_path)