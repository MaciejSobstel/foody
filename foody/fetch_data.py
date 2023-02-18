import psycopg2
from psycopg2 import OperationalError
import math


def fetch_data():
    try:
        conn = psycopg2.connect(
            database="foody",
            user="postgres",
            password="postgres",
            host="localhost")
    except OperationalError as e:
        print(e)
    else:
        cur = conn.cursor()
    cur.execute("SELECT * FROM dishes")
    dishes = cur.fetchall()
    cur.close()
    conn.close()
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
