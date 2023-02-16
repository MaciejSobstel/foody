import psycopg2
from psycopg2 import OperationalError
import random


menu = []


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
    cur.execute("SELECT name, calories, meal_type FROM dishes")
    dishes = cur.fetchall()
    cur.close()
    conn.close()
    return dishes


# def main(calories):
#     calories_start = 0.0


# if __name__ == "__main__":
#     main()

# for record in records:
#     dictionary = {}
#     dictionary[record[0]] = record[2]
#     menu.append(dictionary)


# meals = []
# cals = []
# calories = 0.0
# while calories < 2500.0:
#     random_meal = random.choice(menu)
#     for key, value in random_meal.items():
#         if value != '':
#             calories += float(value)
#             meals.append(key)
#             cals.append(value)


# print(meals)
# print(cals)
