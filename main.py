from src.Brain_Tumor_Classification_MRI import logger
from src.Brain_Tumor_Classification_MRI.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Brain_Tumor_Classification_MRI.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.Brain_Tumor_Classification_MRI.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.Brain_Tumor_Classification_MRI.pipeline.stage_04_model_evaluation_mlflow import EvaluationPipeline
from src.Brain_Tumor_Classification_MRI.config.configuration import ConfigurationManager

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"********************") 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info(f"********************")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "PREPARE BASE MODEL"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info(f"********************")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "MODEL TRAINER"

try:
    logger.info(f"********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    logger.info(f"********************")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "MODEL EVALUATION"

try:
    logger.info(f"********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    logger.info(f"********************")
except Exception as e:
    logger.exception(e)
    raise e