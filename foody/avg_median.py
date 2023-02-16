from foody import fetch_data
import math


def average_dinner():
    num_meals = 0
    calories = 0
    dishes = fetch_data()
    for item in dishes:
        if item[2] == 'dinner':
            if math.isnan(item[1]):
                pass
            else:
                calories += item[1]
                num_meals += 1
    avg_cals = calories / num_meals
    return avg_cals


def average_lunch():
    num_meals = 0
    calories = 0
    dishes = fetch_data()
    for item in dishes:
        if item[2] == 'lunch':
            if math.isnan(item[1]):
                pass
            else:
                calories += item[1]
                num_meals += 1
    avg_cals = calories / num_meals
    return avg_cals


def average_breakfast():
    num_meals = 0
    calories = 0
    dishes = fetch_data()
    for item in dishes:
        if item[2] == 'breakfast':
            if math.isnan(item[1]):
                pass
            else:
                calories += item[1]
                num_meals += 1
    avg_cals = calories / num_meals
    return avg_cals


def median_dinner():
    calories = []
    dishes = fetch_data()
    for item in dishes:
        if item[2] == 'dinner':
            if math.isnan(item[1]):
                pass
            else:
                calories.append(item[1])
    sorted_list = sorted(calories)
    list_len = len(sorted_list)
    middle_index = list_len // 2

    if list_len % 2 == 0:
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        median = sorted_list[middle_index]
    return median


def median_lunch():
    calories = []
    dishes = fetch_data()
    for item in dishes:
        if item[2] == 'lunch':
            if math.isnan(item[1]):
                pass
            else:
                calories.append(item[1])
    sorted_list = sorted(calories)
    list_len = len(sorted_list)
    middle_index = list_len // 2

    if list_len % 2 == 0:
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        median = sorted_list[middle_index]
    return median


def median_breakfast():
    calories = []
    dishes = fetch_data()
    for item in dishes:
        if item[2] == 'breakfast':
            if math.isnan(item[1]):
                pass
            else:
                calories.append(item[1])
    sorted_list = sorted(calories)
    list_len = len(sorted_list)
    middle_index = list_len // 2

    if list_len % 2 == 0:
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        median = sorted_list[middle_index]
    return median
