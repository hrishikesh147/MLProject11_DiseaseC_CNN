
from src.CNNDiseaseClassifier.config.configuration import ConfigurationManager
from src.CNNDiseaseClassifier.components.prepare_base_model import PreparaBaseModel
from src.CNNDiseaseClassifier import logger


STAGE_NAME="Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config=config.get_prepare_base_model_config()
        prepare_base_model=PreparaBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__=="__main__":
    try:
        logger.info(f"stage {STAGE_NAME} started...")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} COMPLETED...")
    except Exception as e:
        raise e