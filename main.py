from src.CNNDiseaseClassifier import logger
from src.CNNDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data_Ingestion_Stage"

try:
    logger.info(f"stage.....{STAGE_NAME} started...")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"stage.....{STAGE_NAME} COMPLETED...")

except Exception as e:
    raise e