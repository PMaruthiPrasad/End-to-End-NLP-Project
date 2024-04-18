from hate.logger import logging
from hate.exception import CustomException
import sys

#logging.info("Welcome to the Project")

#try:
  #  a=7/"0"
#except Exception as e:
    #raise CustomException(e,sys) from e

from hate.configuration.gcloud_syncer import GCloudSync
obj=GCloudSync()
obj.sync_folder_from_gcloud("hate-speech0424",'dataset.zip','download\dataset.zip')
