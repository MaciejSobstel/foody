from avg_median import average, median
from fetch_data import select_from_db


def menu_avg(meal_type=str):
    dishes = select_from_db(meal_type)
    avg_cals = average(meal_type)
    menu = []
    for item in dishes:
        if abs(item[1] - avg_cals) <= 500:
            menu.append(item)
    return menu


def menu_median(meal_type=str):
    dishes = select_from_db(meal_type)
    median_cals = median(meal_type)
    menu = []
    for item in dishes:
        if abs(item[1] - median_cals) <= 500:
            menu.append(item)
    return menu
