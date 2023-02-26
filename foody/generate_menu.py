import argparse
import random
from statistics import mean, median
from typing import Callable, List
import pdb

from fetch_data import select_from_db
from conditions import cond_calories, cond_protein, cond_fat, cond_sodium


def fetch_and_filter_meals(meal_type: str, statistics_callable: Callable = median) -> List:
    all_meals = select_from_db(meal_type)

    # search for meals with 500 calories less or more than median
    requested_calories = statistics_callable([meal[1] for meal in all_meals])
    meal_filter = lambda x: abs(x[1] - requested_calories) <= 500
    return list(filter(meal_filter, all_meals))


def generate_menu(min_calories: float, max_calories: float, min_protein: float, max_protein: float, min_fat: float, max_fat: float, min_sodium: float, max_sodium: float, number_of_breakfasts: int = 1, number_of_lunches: int = 1, number_of_dinners: int = 1):
    if max_calories < 1000.0:
        raise ValueError('Select a number greater than 1000.')
    if max_calories <= min_calories:
        raise ValueError("Maxium calories can't be lower than minimum calories.")
    if max_protein <= min_protein:
        raise ValueError("Maxium protein can't be lower than minimum protein.")
    if max_fat <= min_fat:
        raise ValueError("Maxium fat can't be lower than minimum fat.")
    if max_sodium <= min_sodium:
        raise ValueError("Maxium sodium can't be lower than minimum sodium.")
    if (max_calories - min_calories) < 100:
        raise ValueError("Difference between minimum and maximum calories must be greater than 100.")
    breakfasts = fetch_and_filter_meals('breakfast')
    lunch = fetch_and_filter_meals('lunch')
    dinner = fetch_and_filter_meals('dinner')
    while True:
        meals = [
            random.choice(breakfasts),
            random.choice(lunch),
            random.choice(dinner)
        ]
        for i in range(number_of_breakfasts - 1):
            meals.append(random.choice(breakfasts))
        for i in range(number_of_lunches - 1):
            meals.append(random.choice(lunch))
        for i in range(number_of_dinners - 1):
            meals.append(random.choice(dinner))
        if cond_calories(meals, min_calories, max_calories):
            if cond_protein(meals, min_protein, max_protein):
                if cond_fat(meals, min_fat, max_fat):
                    if cond_sodium(meals, min_sodium, max_sodium):
                        return meals


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser("Generate a menu for a day.")
#     parser.add_argument('min_calories', type=float, help='Minimum number of calories.')
#     parser.add_argument('max_calories', type=float, help='Maximum number of calories.')
#     parser.add_argument('min_protein', type=float, help='Minimum number of protein.')
#     parser.add_argument('max_protein', type=float, help='Maximum number of protein.')
#     parser.add_argument('min_fat', type=float, help='Minimum number of fat.')
#     parser.add_argument('max_fat', type=float, help='Maximum number of fat.')
#     parser.add_argument('min_sodium', type=float, help='Minimum number of sodium.')
#     parser.add_argument('max_sodium', type=float, help='Maximum number of sodium.')
#     parser.add_argument('number_of_breakfasts', type=int, help='Number of breakfasts')
#     parser.add_argument('number_of_lunches', type=int, help='Number of lunches')
#     parser.add_argument('number_of_dinners', type=int, help='Number of dinners')
#     args = parser.parse_args()

#     print(generate_menu(args.min_calories, args.max_calories, args.min_protein, args.max_protein, args.min_fat, args.max_fat, args.min_sodium, args.max_sodium, args.number_of_breakfasts, args.number_of_lunches, args.number_of_dinners))
print(generate_menu(1000, 2000, 1, 200, 1, 200, 1, 200, 2, 2, 2))
