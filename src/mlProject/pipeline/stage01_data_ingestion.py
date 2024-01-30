from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngesion
from mlProject import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngesion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()    

# if __name__=='__main__':
#     try:
#         logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nX<<<<<<<<X")
#     except Exception as e:
#         logger.exception(e)
#         raise e