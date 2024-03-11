from source.entity.config_entity import PipelineConfig
from source.utility.utility import generate_global_timestamp
from source.logger import setup_logger

if __name__ == '__main__':

        global_timestamp = generate_global_timestamp()

        setup_logger(global_timestamp)

        pipeline_obj = PipelineConfig(global_timestamp)
        print(pipeline_obj.__dict__)