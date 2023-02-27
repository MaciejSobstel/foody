from typing import List


def generate_total_value(measured_value: int, meals: List):
    total_value = 0.0
    for meal in meals:
        total_value += meal[measured_value]
    return total_value


def cond(min_value: float, max_value: float, total_value: float) -> bool:
    if total_value >= min_value and total_value <= max_value:
        return True
