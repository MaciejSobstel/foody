import csv
import random


with open('epi_r.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    records = [row for row in csv_reader]


menu = []

for record in records:
    dictionary = {}
    dictionary[record[0]] = record[2]
    menu.append(dictionary)


meals = []
cals = []
calories = 0.0
while calories < 2500.0:
    random_meal = random.choice(menu)
    for key, value in random_meal.items():
        if value != '':
            calories += float(value)
            meals.append(key)
            cals.append(value)


print(meals)
print(cals)