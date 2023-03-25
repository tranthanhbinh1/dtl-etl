import os, logging
from datetime import datetime, timedelta
from workalendar.asia import Singapore
from config.default import ID_FILE_PATH, base_id

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
# Set up a formatter to include timestamp for logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Set up a logger to write logs to a file
file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('job_logging.log')
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)

# Set up a logger to write logs to the console
console_logger = logging.getLogger('console_logger')
console_logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
console_logger.addHandler(stream_handler)

# This was created to help with an error after I installed airflow, still dont know what caused the issue, but this worked
def download_file_helper(url_folder):
    from crawler.manu_job import download_file
    url, destination_folder = url_folder
    download_file(url, destination_folder)

# Checking if the data is available
def check_data_available(url):
    import requests
    response = requests.get(url)
    if "No Record Found" in response.text:
        return False
    return True

# Retrive lastest id
def get_last_id():
    if not os.path.exists(ID_FILE_PATH):
        return None
    with open(ID_FILE_PATH, 'r') as f:
        last_id = f.read().strip()
        return int(last_id) if last_id else None
    
#   Save lastest id
def save_last_id(id):
    with open(ID_FILE_PATH, 'w') as f:
        f.write(str(id))

# Calculate the ID for the given date
def calculate_id(date, base_id):
    start_date = datetime(2023, 3, 20)
    cal = Singapore()
    days_difference = cal.get_working_days_delta(start_date, date)
    if start_date > date:
        days_difference = -days_difference
    id = base_id + days_difference
    return id 

calculate_id(datetime(2023,3,1), base_id)