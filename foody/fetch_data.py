import math

from db_utils.db_connector import db_connector


def fetch_data():
    with db_connector() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dishes")
        dishes = cursor.fetchall()
    return dishes


def select_from_db(meal_type=str):
    dishes = fetch_data()
    selected_dishes = []
    for item in dishes:
        if item[5] == meal_type:
            if math.isnan(item[1]):
                pass
            else:
                selected_dishes.append(item)
    return selected_dishes
