from source.entity.config_entity import PipelineConfig
from source.component.data_ingestion import DataIngestion

class DataPipeline:

    def __init__(self,global_timestamp):
        self.utility_config = PipelineConfig(global_timestamp)

    def start_data_ingestion(self):
        data_ingestion_obj = DataIngestion(self.utility_config)
        data_ingestion_obj.initiate_data_ingestion()

    def run_train_pipeline(self):
        self.start_data_ingestion()