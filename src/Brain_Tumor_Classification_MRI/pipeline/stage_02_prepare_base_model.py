from src.Brain_Tumor_Classification_MRI.config.configuration import ConfigurationManager
from src.Brain_Tumor_Classification_MRI.components.prepare_base_model import PrepareBaseModel
from src.Brain_Tumor_Classification_MRI import logger

STAGE_NAME = "PREPARE BASE MODEL"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        logger.info(f"*******************")
    except Exception as e:
        logger.exception(e)
        raise e