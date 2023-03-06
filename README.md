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
python3 foody/generate_menu.py 1000 2500 1 200 1 200 1 200 2 1 2


Menu: Meyer Lemon and Vanilla Bean Marmalade (breakfast), Mushroom and Tomato Soup (lunch), Linguine and Zucchini with Bagna Cauda Sauce (dinner), Old-Fashioned Raspberry Jam (breakfast), Herbed Jasmine Rice (dinner)
Total calories: 1817.0
Total protein: 27.0
Total fat: 33.0
Total sodium: 175.0
```