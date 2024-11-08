from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging


from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils.main_utils import load_object
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
import os
from sensor.utils.main_utils import read_yaml_file
from sensor.constant.training_pipeline import SAVED_MODEL_DIR


from  fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File, HTTPException,JSONResponse
from sensor.constant.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from fastapi.responses import FileResponse
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
import os
import io
from fastapi import FastAPI, File, UploadFile, Response
import pandas as pd
import tempfile


"""
used to store the temporary output file
"""
with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
    OUTPUT_CSV_PATH = temp_file.name

app = FastAPI()



origins = ["*"]
#Cross-Origin Resource Sharing (CORS) 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/",tags=["authentication"])
async def  index():
    return RedirectResponse(url="/docs")





@app.get("/train")
async def train():
    try:

        training_pipeline = TrainPipeline()

        if training_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        
        training_pipeline.run_pipeline()
        return Response("Training successfully completed!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")
        

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Check if uploaded file is a CSV
        if file.content_type != 'text/csv':
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
        
        # Read the uploaded CSV file
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))

        # Check if model exists
        Model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not Model_resolver.is_model_exists():
            return JSONResponse(content={"error": "Model is not available"}, status_code=404)

        # Load the best model and predict
        best_model_path = Model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)
        
        # Add predictions to the DataFrame and map target values
        df['predicted_column'] = y_pred
        reverse_mapping = TargetValueMapping().reverse_mapping()
        df['predicted_column'].replace(reverse_mapping, inplace=True)
        
        # Save results to a temporary CSV file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
            output_csv_path = temp_file.name
            df.to_csv(output_csv_path, index=False)
        
        # Return the temporary CSV file as a response
        return FileResponse(path=output_csv_path, filename="predictions_with_test_data.csv", media_type="text/csv")

    except Exception as e:
        raise  SensorException(e,sys)




def main():
    try:
            
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)



if __name__ == "__main__":

    app_run(app ,host=APP_HOST,port=APP_PORT)







  











