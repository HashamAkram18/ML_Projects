import sys

from src.MLproject.exception import CustomException
from src.MLproject.logger import logging
from src.MLproject.components.data_ingestion import DataIngestion,DataIngestionConfig
from src.MLproject.components.data_transformation import DataTransformationconfig,DataTransformation
from src.MLproject.components.model_trainer import ModelTrainerConfig,ModelTrainer 


if __name__=="__main__":
    logging.info("The Execution has started")

    try:
        data_ingestion = DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
     
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        
        ## Model Training
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))


    except Exception as e:
        logging.info("Custom Exception")    
        raise CustomException(sys,e)