from typing import List


def total_value(measured_value: int, meals: List):
    total_value = 0.0
    for meal in meals:
        total_value += meal[measured_value]
    return total_value


def cond_calories(meals: List, min_calories: float, max_calories: float) -> bool:
    total_calories = total_value(1, meals)
    if total_calories >= min_calories and total_calories <= max_calories:
        return True


def cond_protein(meals: List, min_protein: float, max_protein: float) -> bool:
    total_protein = total_value(2, meals)
    if total_protein >= min_protein and total_protein <= max_protein:
        return True


def cond_fat(meals: List, min_fat: float, max_fat: float) -> bool:
    total_fat = total_value(3, meals)
    if total_fat >= min_fat and total_fat <= max_fat:
        return True


def cond_sodium(meals: List, min_sodium: float, max_sodium: float) -> bool:
    total_sodium = total_value(4, meals)
    if total_sodium >= min_sodium and total_sodium <= max_sodium:
        return True
