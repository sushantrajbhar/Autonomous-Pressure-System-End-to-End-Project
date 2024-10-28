from dataclasses import dataclass
import os
import pymongo
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


"""
Dataclass is used to store the values in variables. Hence we create a decorator and also store 
the environment variables.

"""
@dataclass


class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")



env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)