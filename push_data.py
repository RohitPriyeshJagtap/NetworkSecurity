import os 
import sys 
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
import pymongo.mongo_client
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca=certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records= list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongo(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records= records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == "__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE = "network_security"
    Collection = "NetworkData"
    network_obj=NetworkDataExtract()
    records=network_obj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records= network_obj.insert_data_to_mongo(records=records,database=DATABASE, collection=Collection)
    print(f"Total number of records inserted: {no_of_records}")


