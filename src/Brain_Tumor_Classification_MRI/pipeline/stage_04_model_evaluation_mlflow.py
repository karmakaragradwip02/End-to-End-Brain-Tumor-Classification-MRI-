from Brain_Tumor_Classification_MRI.config.configuration import ConfigurationManager
from Brain_Tumor_Classification_MRI.components.model_evaluation_mlflow import Evaluation
from Brain_Tumor_Classification_MRI import logger


STAGE_NAME = "MODEL EVALUATION"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

if __name__ == '__main__':
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