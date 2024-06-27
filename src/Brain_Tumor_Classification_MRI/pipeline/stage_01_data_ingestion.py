from src.Brain_Tumor_Classification_MRI.config.configuration import ConfigurationManager
from src.Brain_Tumor_Classification_MRI.components.data_ingestion import DataIngestion
from src.Brain_Tumor_Classification_MRI import logger

STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    

if __name__ == '__name__':
    try: 
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e