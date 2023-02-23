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
usage: Generate a menu for a day. [-h] min_calories max_calories

positional arguments:
  min_calories  Minimum number of calories.
  max_calories  Maximum number of calories.

options:
  -h, --help    show this help message and exit
```

```
python3 foody/generate_menu.py 1200 1500

[('Smoked Salmon and Leek Scramble with Meyer Lemon Crème Fraîche ', 393.0, 21.0, 31.0, 1008.0, 'breakfast'), ('Nantucket Scallop Chowder ', 490.0, 27.0, 36.0, 1576.0, 'lunch'), ('Fresh Corn Soup Topped with Roasted Corn Guacamole ', 374.0, 10.0, 21.0, 1324.0, 'dinner')]
```