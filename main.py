from mlProject import logger
from mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Welcome to our custom logging")
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nX<<<<<<<<X")
except Exception as e:
    logger.exception(e)
    raise e
