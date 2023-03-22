import os, logging


#get path
current_path = os.getcwd()

# Create folders
def create_folder():
    list = ['tick', "tickDs", "tradeCancel", "tradeCancelDs"]
    for items in list:
        try:
            path = os.path.join(current_path, "data", items)
            os.makedirs(path)
        except FileExistsError:
            break

# Loggers
# Set up a logger to write logs to a file
file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('job_logging.log')
file_logger.addHandler(file_handler)

# Set up a logger to write logs to the console
console_logger = logging.getLogger('console_logger')
console_logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
console_logger.addHandler(stream_handler)