import os
from datetime import datetime
from source.constant import constant
from source.constant.constant import MONGODB_KEY

class PipelineConfig:
    def __init__(self,global_timestamp):
        self.global_timestamp = global_timestamp
        self.artifact_dir = os.path.join(constant.ARTIFACT_DIR,global_timestamp)
        self.target_column = constant.TARGET_COLUMN
        self.train_pipeline_name = constant.TRAIN_PIPELINE_NAME
        self.mongodb_url_key = constant.MONGODB_URL_KEY
        #self.mongodb_url_key = os.environ.get(MONGODB_KEY)
        #self.mongodb_url_key = os.environ[constant.MONGODB_KEY]
        self.aws_access_key = constant.AWS_ACCESS_KEY
        self.aws_secret_key = constant.AWS_SECRET_KEY
        self.aws_region = constant.AWS_REGION
        self.aws_bucket_name = constant.AWS_BUCKET_NAME
        self.aws_bucket_prefix = constant.AWS_BUCKET_PREFIX

        self.database_name = constant.DATABASE_NAME
        self.train_test_split_ratio = constant.DI_TRAIN_TEST_SPLIT_RATIO
        self.train_collection_name = constant.TRAIN_DI_COLLECTION_NAME
        self.di_dir = os.path.join(self.artifact_dir,constant.DI_DIR_NAME)
        #self.train_feature_store_file_path = os.path.join(self.di_dir,constant.DI_FEATURE_STORE_DIR,constant.FILENAME)
        self.train_feature_store_dir_path = os.path.join(self.artifact_dir,self.train_pipeline_name,constant.DI_DIR_NAME,constant.DI_FEATURE_STORE_DIR)
        self.train_feature_store_file_name = constant.FILENAME

        self.train_di_train_file_path = os.path.join(self.artifact_dir, self.train_pipeline_name, constant.DI_DIR_NAME,constant.DI_INGESTED_DIR)
        self.train_di_test_file_path = os.path.join(self.artifact_dir, self.train_pipeline_name, constant.DI_DIR_NAME,constant.DI_INGESTED_DIR)
        #self.train_filename = os.path.join(self.di_dir,constant.DI_INGESTED_DIR,constant.TRAIN_FILE_NAME)
        #self.test_filename = os.path.join(self.di_dir, constant.DI_INGESTED_DIR, constant.TEST_FILE_NAME)
        self.mandatory_col_list = constant.DI_MANDATORY_COLUMN_LIST
        self.mandatory_col_data_type = constant.DI_MANDATORY_COLUMN_DATA_TYPE

        self.imputation_values_file = constant.DV_IMPUTATION_VALUES_FILE_NAME
        self.outlier_params_file = constant.DV_OUTLIER_PARAMS_FILE
        self.train_dv_imputation_values_file_path = constant.DV_IMPUTATION_FILE_PATH
        self.train_dv_imputation_values_file_name = constant.DV_IMPUTATION_FILE_NAME
        self.train_file_name = constant.TRAIN_FILE_NAME
        self.test_file_name = constant.TEST_FILE_NAME

        self.train_dv_imputation_values_file_name = constant.DV_IMPUTATION_VALUES_FILE_NAME

        self.train_dv_train_file_path = os.path.join(self.artifact_dir, self.train_pipeline_name, constant.DV_DIR_NAME)
        self.train_dv_test_file_path = os.path.join(self.artifact_dir, self.train_pipeline_name, constant.DV_DIR_NAME)

        self.dv_train_file_path = os.path.join(self.artifact_dir,constant.DV_DIR_NAME)
        self.dv_test_file_path = os.path.join(self.artifact_dir, constant.DV_DIR_NAME)

        self.dt_binary_class_col = constant.DT_BINARY_CLASS_COL
        self.dt_multi_class_col = constant.DT_MULTI_CLASS_COL
        self.dt_multi_class_encoder = constant.DT_ENCODER_PATH

        self.dt_train_file_path = os.path.join(self.artifact_dir, constant.DT_DIR_NAME)
        self.dt_test_file_path = os.path.join(self.artifact_dir, constant.DT_DIR_NAME)

        self.train_dt_train_file_path = os.path.join(self.artifact_dir, self.train_pipeline_name, constant.DT_DIR_NAME)
        self.train_dt_test_file_path = os.path.join(self.artifact_dir, self.train_pipeline_name, constant.DT_DIR_NAME)

        # model train and evaluate
        self.model_path = os.path.join(constant.MODEL_PATH)
        self.final_model_path = os.path.join(constant.FINAL_MODEL_PATH)

        #self.predict_di_dir = os.path.join(self.artifact_dir, constant.PREDICT_PIPELINE_NAME, constant.DI_DIR_NAME)

        self.predict_di_dir = os.path.join(self.artifact_dir, constant.PREDICT_PIPELINE_NAME, constant.DI_DIR_NAME)

        #self.predict_di_feature_store_file_path = os.path.join(self.predict_di_dir, constant.PREDICT_DATA_FILE_NAME)
        # self.predict_di_feature_store_file_path = os.path.join(self.predict_di_dir,constant.DI_FEATURE_STORE_DIR)
        # self.predict_di_feature_store_file_name = constant.PREDICT_DATA_FILE_NAME

        self.predict_di_feature_store_file_path = os.path.join(self.predict_di_dir, constant.DI_FEATURE_STORE_DIR)
        self.predict_di_feature_store_file_name = constant.PREDICT_DATA_FILE_NAME

        self.predict_dv_file_path = os.path.join(self.artifact_dir, constant.PREDICT_PIPELINE_NAME,
                                                 constant.DV_DIR_NAME)
        self.predict_dt_file_path = os.path.join(self.artifact_dir, constant.PREDICT_PIPELINE_NAME,
                                                 constant.DT_DIR_NAME)
        self.predict_collection_name = constant.PREDICT_DI_COLLECTION_NAME

        self.di_col_drop_in_clean = constant.DI_COL_DROP_IN_CLEAN
        self.predict_file = constant.PREDICT_FILE
        self.predict_file_path = os.path.join(self.predict_di_dir, constant.DI_INGESTED_DIR)

        self.predict_mp_file_path = os.path.join(self.artifact_dir, constant.PREDICT_PIPELINE_NAME, constant.MP_DIR_NAME)
        self.final_model_file_name = constant.FINAL_MODEL_FILE_NAME

        self.aws_access_key = constant.AWS_ACCESS_KEY
        self.aws_secret_key = constant.AWS_SECRET_KEY
        self.aws_region = constant.AWS_REGION
        self.aws_bucket_name = constant.AWS_BUCKET_NAME
        self.aws_bucket_prefix = constant.AWS_BUCKET_PREFIX







