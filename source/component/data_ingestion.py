import os
import logging

import pandas as pd
from sklearn.model_selection import train_test_split
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

    def split_data_train_test(self,data):
        try:
            logging.info("start: train,test data split")

            train_set ,test_set = train_test_split(data,train_size=self.utility_config.train_test_split_ratio,random_state=45)

            dir_path = os.path.dirname(self.utility_config.train_filename)
            os.makedirs(dir_path,exist_ok=True)

            train_set.to_csv(self.utility_config.train_filename,index=False)
            test_set.to_csv(self.utility_config.test_filename, index=False)

            logging.info("complete: train,test data split")
        except ChurnException as e:
            raise e

    def clean_data(self,data):
        try:
            logging.info("Start : clean data")

            data = data.drop_duplicates()

            data = data.loc[:, data.nunique() > 1]

            drop_column = []

            for col in data.select_dtypes(include=['object']).columns:

                unique_count = data[col].nunique()

                if unique_count / len(data) > 0.5:
                    data.drop(col,axis=1,inplace = True)
                    drop_column.append(col)

            logging.info(f"dropped columns: {drop_column}")
            logging.info("Complete : clean data")
            return data
        except ChurnException as e:
            raise e

    def process_data(self,data):
        try:
            logging.info("Start: process data")

            for col in self.utility_config.mandatory_col_list :

                if col not in data.columns:

                    raise ChurnException (f"missing columns {col}")

                if data[col].dtype != self.utility_config.mandatory_col_data_type:

                    try:
                        data[col] = data[col].astype(self.utility_config.mandatory_col_data_type[col])

                    except ChurnException as e:
                        raise ChurnException(f"error converting the data type for the column {col}")

            logging.info("Complete: process data")

            return data
        except ChurnException as e:
            raise e

    def initiate_data_ingestion(self):
        data = self.export_data_into_feature_store()
        data = self.clean_data(data)
        data = self.process_data(data)
        self.split_data_train_test(data)