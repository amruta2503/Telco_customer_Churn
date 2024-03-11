import os
import logging

import pandas as pd
from pymongo.mongo_client import MongoClient
from source.exception import ChurnException

class DataIngestion:
    def __init__(self,utility_config):
        self.utility_config = utility_config

    def export_data_into_feature_store(self):
        try:
            logging.info("start:data ingestion")

            client = MongoClient(self.utility_config.mongodb_url_key)
            database = client[self.utility_config.database_name]
            collection = database[self.utility_config.collection_name]

            cursor = collection.find()

            data = pd.DataFrame(list(cursor))

            dir_path = os.path.dirname(self.utility_config.feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            data.to_csv(self.utility_config.feature_store_file_path,index=False)

            logging.info("complete:data ingestion")

            return data
        except ChurnException as e:
            raise e

    def split_data_train_test(self):
        pass

    def clean_data(self):
        pass

    def process_data(self):
        pass

    def initiate_data_ingestion(self):
        data = self.export_data_into_feature_store()
        self.split_data_train_test()