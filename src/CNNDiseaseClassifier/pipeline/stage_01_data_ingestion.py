from src.CNNDiseaseClassifier.config.configuration import ConfigurationManager
from src.CNNDiseaseClassifier.components.data_ingestion import DataIngestion
from src.CNNDiseaseClassifier import logger

STAGE_NAME="Data_Ingestion_Stage"

class DataIngestionTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_files()
        data_ingestion.extract_zip_file()

        
if __name__=="__main__":
    try:
        logger.info(f"stage.....{STAGE_NAME} started...")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"stage.....{STAGE_NAME} COMPLETED...")

    except Exception as e:
        raise e

