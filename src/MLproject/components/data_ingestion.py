import os 
import sys
from src.MLproject.exception import CustomException
from src.MLproject.logger import logging
import pandas as pd 
from src.MLproject.utils import read_MySql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('Artifacts', 'train.csv')
    test_data_path:str=os.path.join('Artifacts', 'test.csv')
    raw_data_path:str=os.path.join('Artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # code to read form the mysql data
            df=read_MySql_data()
            logging.info("Reading completed from MySQL database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path))
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # code to split and train-test data
            train_set, test_set = train_test_split(df,test_size=0.2, random_state=45 )
            df.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            df.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion is completed") 

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)    