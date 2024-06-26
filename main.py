from source.entity.config_entity import PipelineConfig
from source.utility.utility import generate_global_timestamp
from source.logger import setup_logger
from source.logger import logging
from source.pipeline.pipeline import DataPipeline

from source.constant.constant import APP_HOST,APP_PORT

from fastapi import FastAPI, Response
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as app_run

app = FastAPI()
origins = ['*']

app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_credentials = True,
        allow_methods = ['*'],
        allow_headers = ['*']
)

def run_pipeline(pipeline_type):

        try :
                global_timestamp = generate_global_timestamp()

                setup_logger(global_timestamp)

                pipeline_obj = DataPipeline(global_timestamp)
                logging.info(f"start: Model {pipeline_type.upper()}")

                if pipeline_type == 'training':
                        pipeline_obj.run_train_pipeline()
                elif pipeline_type == 'prediction':
                        pipeline_obj.run_predict_pipeline()

                logging.info(f"END:Model {pipeline_type.upper()} ")

                print(f"model {pipeline_type} complete")

                return f"model {pipeline_type} complete"
        except Exception as e:
                return f"Error occurred {e}"


@app.get('/',tags=['authentication'])
async def index():
        return RedirectResponse(url="/docs")

@app.get("/train",tags = ['pipeline'])
async def train_route():
        main('training')
        return  {"message : 'training pipeline start"}

@app.get('/predict',tags = ['pipeline'])
async def predict_route():
        main('prediction')
        return {"message : 'prediction pipeline start"}

def main(pipeline_type):
        try:
                global_timestamp =  generate_global_timestamp()
                setup_logger(global_timestamp)
                run_pipeline(pipeline_type)
        except Exception as e:
                print(e)
                logging.info(e)


if __name__ == '__main__':

        # global_timestamp = generate_global_timestamp()
        #
        # setup_logger(global_timestamp)
        #
        # logging.info("setup global timestamp")
        #
        # # pipeline_obj = PipelineConfig(global_timestamp)
        # # print(pipeline_obj.__dict__)
        #
        # pipeline_obj = DataPipeline(global_timestamp)
        # #pipeline_obj.run_train_pipeline()
        #
        # pipeline_obj.run_predict_pipeline()


        app_run(app,host=APP_HOST,port= APP_PORT)
