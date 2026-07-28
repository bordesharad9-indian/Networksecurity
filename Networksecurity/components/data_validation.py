from Networksecurity.entity.artifact_entity import DataIngestionArtifact , DataValidationArtifact
from Networksecurity.entity.config_entity import DataValidationConfig
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logger
from scipy.stats import ks_2samp
import pandas as pd
import os,sys
from Networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from Networksecurity.utils.main_utils.utils import read_yaml_file


class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationArtifact):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self.__schema_config=read_yaml_file(SCHEMA_FILE_PATH)
           
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns=len(self.__schema_config)
            logger.info(f"Required number of columns:{number_of_columns}")
            logger.info(f"Data frame has columns:{dataframe.columns}")
            if len(dataframe.columns)==number_of_columns:
                return True
            return False
        except Exception as e:
            raise NetworkSecurityException(e,sys)





    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path=self.data_ingestion_artifact.trained_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            ## read the data from train and test
            train_dataframe=DataValidation.read_data(file_path=train_file_path)
            test_dataframe=DataValidation.read_data(file_path=test_file_path)

            ##validate number of columns
            status=self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message=f" train dataframe does not contain all columns"


            status=self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                 error_message=f" train dataframe does not contain all columns"



        except Exception as e:
            raise NetworkSecurityException(e,sys)

