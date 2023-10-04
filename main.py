from src.CNNDiseaseClassifier import logger
from src.CNNDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CNNDiseaseClassifier.pipeline.stage02_prepare_basemodel import PrepareBaseModelTrainingPipeline
from src.CNNDiseaseClassifier.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME="Data_Ingestion_Stage"
try:
    logger.info(f"stage.....{STAGE_NAME} started...")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"stage.....{STAGE_NAME} COMPLETED...")

except Exception as e:
    raise e


STAGE_NAME="Prepare Base Model  Stage"
try:
    logger.info(f"stage {STAGE_NAME} started...")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} COMPLETED...")

except Exception as e:
    raise e


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


