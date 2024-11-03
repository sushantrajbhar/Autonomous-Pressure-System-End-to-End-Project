import os

"""
These are the constants that would be there for training the dataset
"""

TARGET_COLUMN = "class"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
FILE_NAME = "sensor.csv"

"""In the data Ingestion artifact, there would be folder created
 called feature store and in the folder, sensor.csv would be created """

TRAIN_FILE_NAME:str="train.csv" 
TEST_FILE_NAME:str="test.csv"

#pre-processing related constants
PREPROCESSING_OBJECT_FILE_NAME="preprocessor.pkl"
MODEL_FILE_NAME="model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS="drop_columns"


#Data Ingestion related constants

DATA_INGESTION_COLLECTION_NAME:str="mongoclass"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2


#Data Validation related constants

DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_DIR:str="validated"
DATA_VALIDATION_INVALID_DIR:str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"
