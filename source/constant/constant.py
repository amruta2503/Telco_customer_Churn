import os


APP_HOST = '0.0.0.0'
APP_PORT = 8000

ARTIFACT_DIR = "dev-tcc-artifact"
TRAIN_PIPELINE_NAME = "train"
TARGET_COLUMN = "Churn"
FILENAME = "train_data.csv"

MONGODB_KEY = "MONGODB_URL"

MONGODB_URL_KEY = "mongodb+srv://amrutasharnangat2503:eQI1fsJVp1Jtx6M0@cluster0.r6fy3lw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = 'db-customer-churn'
TRAIN_DI_COLLECTION_NAME = 'telco-customer-churn'

#MONGODB_URL_KEY = "mongodb+srv://sanjay:C7H1U0YpnqhWYYci@cluster0.cmp0dtp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#MONGODB_URL_KEY = "mongodb+srv://amrutasharnangat2503:mongo@cluster0.r6fy3lw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
#MONGODB_URL_KEY = "mongodb+srv://clarityai:N0lTZ4zedDxGbn9N@cluster0.qketnjc.mongodb.net/?retryWrites=true&w=majority"
DI_DIR_NAME = "data_ingestion"
DI_INGESTED_DIR = "ingested"
DI_TRAIN_TEST_SPLIT_RATIO = 0.2
DI_FEATURE_STORE_DIR = "feature_store"

DI_MANDATORY_COLUMN_LIST = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
                       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
                       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
                       'MonthlyCharges', 'TotalCharges', 'Churn']

DI_MANDATORY_COLUMN_DATA_TYPE = {'gender': 'object', 'SeniorCitizen': 'object', 'Partner': 'object',
                              'Dependents': 'object', 'tenure': 'int64', 'PhoneService': 'object',
                              'MultipleLines': 'object', 'InternetService': 'object', 'OnlineSecurity': 'object',
                              'OnlineBackup': 'object', 'DeviceProtection': 'object', 'TechSupport': 'object',
                              'StreamingTV': 'object', 'StreamingMovies': 'object', 'Contract': 'object',
                              'PaperlessBilling': 'object', 'PaymentMethod': 'object', 'MonthlyCharges': 'float64',
                              'TotalCharges': 'float64', 'Churn': 'object'}

DV_IMPUTATION_VALUES_FILE_NAME  = "source/ml/imputation_values.csv"
DV_IMPUTATION_FILE_PATH = "source/ml"
DV_IMPUTATION_FILE_NAME = "imputation_values.csv"

DV_OUTLIER_PARAMS_FILE = "source/ml/outlier_details.csv"
DV_DIR_NAME = "data_validation"

DT_MULTI_CLASS_COL = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']
DT_BINARY_CLASS_COL = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'gender']
DT_ENCODER_PATH = 'source/ml/multi_class_encoder.pkl'

DT_DIR_NAME: str = "data_transformation"
FINAL_MODEL_PATH = "source/ml/final_model"
MODEL_PATH = "source/ml/artifact"

PREDICT_PIPELINE_NAME = 'predict'
PREDICT_DATA_FILE_NAME = 'predict_data.csv'

PREDICT_DI_COLLECTION_NAME = "predict-telco-customer-churn"

DI_COL_DROP_IN_CLEAN = ['_id','customerID']
PREDICT_FILE = 'predict.csv'

MP_DIR_NAME = "model_prediction"
FINAL_MODEL_FILE_NAME = "GradientBoostingClassifier.pkl"

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
AWS_REGION = os.environ['AWS_REGION']

AWS_BUCKET_NAME = 'test-churn-demo1'
AWS_BUCKET_PREFIX = "dev-tcc-artifact"
