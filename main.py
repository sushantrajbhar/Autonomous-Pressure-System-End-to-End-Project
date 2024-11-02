from sensor.exception import SensorException
import os
import sys
from sensor.logger import logging
from sensor.configuration.mongo_db_connection  import MongoDBClient

from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection
from sensor.pipeline.training_pipeline import TrainPipeline



# if __name__=="__main__":
#     file_path=r"C:\Users\HP\Desktop\Learn Machine Learning\Learn Machine Learning\Projects for Resume\2. Autonomous Pressure System\Autonomous-pressure-system-End-to-End-project\Dataset\aps_failure_training_set1.csv"
#     database_name="APS"
#     collection_name="mongoclass"
#     dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)

# def test_exception():
#     try:
#         logging.info("Welcome to the project")
#         a=1/0
#     except Exception as e:
#         raise SensorException(e,sys)


# if __name__=="__main__":
#     try:
#         test_exception()
#     except Exception as e:
#         print(e)

if __name__ == "__main__":


    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()