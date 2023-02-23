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

3. Migrate data
- Download data from [kaggle](https://www.kaggle.com/datasets/hugodarwood/epirecipes?resource=download)
- Unpack data
```bash
unzip <DATA_DIR>/archive.zip epi_r.csv -d .
```
- 
```bash
python3 db_utils/postrgresql_database.py --csv_path epi_r.csv
```