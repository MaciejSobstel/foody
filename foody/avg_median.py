from fetch_data import select_from_db


def average(meal_type=str):
    num_meals = 0
    calories = 0
    dishes = select_from_db(meal_type)
    for item in dishes:
        calories += item[1]
        num_meals += 1
    avg_cals = calories / num_meals
    return avg_cals


def median(meal_type=str):
    selected_dishes = select_from_db(meal_type)
    calories = []
    for item in selected_dishes:
        calories.append(item[1])
    sorted_list = sorted(calories)
    list_len = len(sorted_list)
    middle_index = list_len // 2
    if list_len % 2 == 0:
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        median = sorted_list[middle_index]
    return median


if __name__ == "__main__":
    print(f"avg dinner - {average('dinner')}\n"
          f"avg breakfast - {average('breakfast')}\n"
          f"avg lunch - {average('lunch')}\n"
          f"median dinner - {median('dinner')}\n"
          f"median breakfast - {median('breakfast')}\n"
          f"median lunch - {median('lunch')}\n")
