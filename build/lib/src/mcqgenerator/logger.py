import logging
import os
from datetime import datetime
# from mcqgenerator.config import LOG_FILE

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  
# Inside LOG_FILE file we will store all the logs information 
# datetime.now = current date and time
# strftime = format the date and time
# LOG_FILE = name of the file
# m_%d_%Y_%H_%M_%S = format of the date and time
# .log = extension of the file

logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
# os.makedirs = create a directory
# exist_ok = if the directory already exists then it will not raise an error
# os.getcwd = get the current working directory
# join = join the path
# logs = name of the directory
# path = path of the directory

LOG_FILEPATH = os.path.join(logs_path, LOG_FILE)
# os.path.join = join the path
# logs_path = path of the directory
# LOG_FILE = name of the file
# LOG_FILEPATH = path of the file

logging.basicConfig(
    filename=LOG_FILEPATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# logging.basicConfig = set the basic configuration of the logger
# filename = name of the file
# format = format of the file
# level = level of the file
# logging.INFO = level of the file
# LOG_FILEPATH = path of the file
# %(asctime)s = current date and time
# %(lineno)d = line number
# %(name)s = name of the file
# %(levelname)s = level of the file
# %(message)s = message of the file


# To test this 'logger.py' file , we are going to create 'test.py' file
# and import this 'logger.py' file
# and run this 'test.py' file