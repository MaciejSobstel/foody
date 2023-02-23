from contextlib import contextmanager

import psycopg2
from psycopg2 import OperationalError

from dotenv import dotenv_values

config = dotenv_values()

@contextmanager
def db_connector():
    try:
        conn = psycopg2.connect(
            database=config["DB_NAME"],
            user=config["DB_USER"],
            password=config["DB_PASSWORD"],
            host=config["DB_HOST"],
            port=config["DB_PORT"])
    except OperationalError as e:
        print(e)
    else:
        yield conn
    finally:
        if conn:
            conn.close()