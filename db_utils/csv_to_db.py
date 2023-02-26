import argparse
from pathlib import Path

from db_connector import db_connector

from read_csv import read_csv


def migrate(csv_path: Path):
    with db_connector() as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dishes (name TEXT, calories FLOAT, protein FLOAT, fat FLOAT, sodium FLOAT, meal_type TEXT)")
        conn.commit()
        dishes = read_csv(csv_path)
        for item in dishes:
            cursor.execute(f"INSERT INTO dishes (name, calories, protein, fat, sodium, meal_type) VALUES ('{item['title']}', '{item['calories']}', '{item['protein']}', '{item['fat']}', '{item['sodium']}', '{item['meal_type']}')")
        conn.commit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Migrate csv to postgresql")
    parser.add_argument("--csv_path", type=Path, required=True)
    args = parser.parse_args()

    migrate(args.csv_path)
