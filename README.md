# foody
Meal Plan Generator Application for Calorie and Macronutrient Requirements

## Prerequisites
1. Postgres database

## Setup
1. Install requirements
```
pip install -r requirements.txt
```

2. Setup db connection credentials in '.env`, for example:
```
DB_NAME=foody
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

3. Install packages
```bash
pip install -e .
```

4. Migrate data
- Download data from [kaggle](https://www.kaggle.com/datasets/hugodarwood/epirecipes?resource=download)
- Unpack data
```bash
unzip <DATA_DIR>/archive.zip epi_r.csv -d .
```
-
```bash
python3 db_utils/csv_to_db.py --csv_path epi_r.csv
```

## Usage
```bash
usage: Generate a menu for a day. [-h] min_calories max_calories min_protein max_protein min_fat max_fat min_sodium max_sodium number_of_breakfasts number_of_lunches number_of_dinners

positional arguments:
  min_calories  Minimum number of calories.
  max_calories  Maximum number of calories.
  min_protein Minimum number of protein.
  max_protein Maximum number of protein.
  min_fat  Minimum number of fat.
  max_fat  Maximum number of fat.
  min_sodium  Minimum number of sodium.
  max_sodium  Maximum number of sodium.
  number_of_breakfasts Number of breakfasts.
  number_of_lunches Number of lunches.
  number_of_dinners Number of dinners.

options:
  -h, --help    show this help message and exit
```

```
python3 foody/generate_menu.py 1000 5500 1 200 1 200 1 4000 3 2 2


Menu:
Rösti with Black Forest Ham and Chives (breakfast),
Smoked Salmon Chowder (lunch),
Green-Curry Chicken with Peas and Basil (dinner),
Coffee-Glazed Doughnuts (breakfast),
Dried Fruit Stewed with Brown Sugar and Vanilla (breakfast),
Shrimp and Avocado Salad with Grapefruit Vinaigrette (lunch),
Black Pepper Spice-Rubbed Beef Tenderloin (dinner)
Total calories: 2800.0
Total protein: 135.0
Total fat: 168.0
Total sodium: 2926.0
```

## GUI Usage

    Minimim calories slider - select minimum number of calories from 500 to 3000.

    Maximum calories slider - select maximum number of calories from 1000 to 5000.

    Minimum protein slider - select minimum number of protein from 1 to 200.

    Maximum protein slider - select maximum number of protein from 1 to 200.

    Minimum fat slider - select minimum number of fat from 1 to 200.

    Maximum fat slider - select maximum number of fat from 1 to 200.

    Minimum sodium slider - select minimum number of sodium from 1 to 3000.

    Maximum sodium slider - select maximum number of sodium from 1000 to 5000.

    Number of breakfasts spinbox - select number of breakfasts from 1 to 5 by using adjacent buttons to increment or decrement the spinbox value.

    Number of lunches spinbox - select number of lunches from 1 to 5 by using adjacent buttons to increment or decrement the spinbox value.

    Number of dinners spinbox - select number of dinners from 1 to 5 by using adjacent buttons to increment or decrement the spinbox value.

    Generate my menu! button - returns the selected number of meals with selected macronutriens.