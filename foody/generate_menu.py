import argparse
import random
from statistics import mean, median
from typing import Callable, List

from fetch_data import select_from_db

def fetch_and_filter_meals(meal_type: str, statistics_callable: Callable = median) -> List:
    all_meals = select_from_db(meal_type)

    # search for meals with 500 calories less or more than median
    requested_calories = statistics_callable([meal[1] for meal in all_meals]) 
    meal_filter = lambda x: abs(x[1] - requested_calories) <= 500
    return list(filter(meal_filter, all_meals))

def generate_menu(min_calories: float, max_calories: float, number_of_meals: int = 3):
    if max_calories < 1000.0:
        raise ValueError('Select a number greater than 1000.')
    
    breakfasts = fetch_and_filter_meals('breakfast')
    lunch = fetch_and_filter_meals('lunch')
    dinner = fetch_and_filter_meals('dinner')

    total_calories = lambda x: sum([meal[1] for meal in x])

    while True:
        meals = [
            random.choice(breakfasts),
            random.choice(lunch),
            random.choice(dinner)
        ]
        if total_calories(meals) >= min_calories and total_calories(meals) <= max_calories:
            return meals


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Generate a menu for a day.")
    parser.add_argument('min_calories', type=float, help='Minimum number of calories.')
    parser.add_argument('max_calories', type=float, help='Maximum number of calories.')
    args = parser.parse_args()

    print(generate_menu(args.min_calories, args.max_calories))