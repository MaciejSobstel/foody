import random

from menu import menu_median


def main(min_calories, max_calories):
    max_calories = float(max_calories)
    min_calories = float(min_calories)
    if max_calories < 1000.0:
        print('Select a number greater than 1000.')
    else:
        menu_dinner = menu_median('dinner')
        menu_breakfast = menu_median('breakfast')
        menu_lunch = menu_median('lunch')
        meals = []
        while len(meals) < 3:
            dinner = random.choice(menu_dinner)
            breakfast = random.choice(menu_breakfast)
            lunch = random.choice(menu_lunch)
            chosen_meals = [breakfast, lunch, dinner]
            if sum([meal[1] for meal in chosen_meals]) <= max_calories and sum([meal[1] for meal in chosen_meals]) >= min_calories:
                meals.extend(chosen_meals)
                return meals
            else:
                main(min_calories, max_calories)


if __name__ == '__main__':
    print(main(input("At least how many calories should you consume daily? "), input("At most how many calories should you consume daily? ")))
