import os 
import sys
from src.MLproject.exception import CustomException
from src.MLproject.logger import logging
import pandas as pd 
import pymysql
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_MySql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established", mydb)
        df=pd.read_sql_query('SELECT * FROM students', mydb)
        print(df.head)

        return df
    

    except Exception as ex:
        raise CustomException(ex)
