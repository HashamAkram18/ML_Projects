import sys
from src.MLproject.exception import CustomException
from src.MLproject.logger import logging
from src.MLproject.components.data_ingestion import DataIngestion
from src.MLproject.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("The Execution has started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
     
    except Exception as e:
        logging.info("Custom Exception")    
        raise CustomException(e, sys)