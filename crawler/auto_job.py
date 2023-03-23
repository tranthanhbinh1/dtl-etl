import wget, os, requests
from datetime import datetime, date
from multiprocessing import Pool
from config.default import get_urls_folders, base_id, ID_FILE_PATH
from utils.utils import create_folder, current_path, file_logger, download_file_helper, check_data_available

def get_last_id():
    if not os.path.exists(ID_FILE_PATH):
        return None
    with open(ID_FILE_PATH, 'r') as f:
        last_id = f.read().strip()
        return int(last_id) if last_id else None

def save_last_id(id):
    with open(ID_FILE_PATH, 'w') as f:
        f.write(str(id))


def download_file(url, destination_folder):
    if check_data_available(url) == False:
        file_logger.error("No Record Found")
        return
    destination_path = os.path.join(current_path, destination_folder)
    try:
        wget.download(url, out=destination_path)
        file_logger.info(f'Successfully downloaded {url}')
    except Exception as e:
        file_logger.error(f'Error downloading {url}: {e}')
    

if __name__ == "__main__":
    create_folder()

    last_id = get_last_id()
    if last_id is None:
        # First run, use base id
        id = base_id
    else:
        # Increment last id by 1
        id = last_id + 1
    # Save the current id for next run
    if check_data_available(get_urls_folders(id)[0][0]):
        save_last_id(id)

    urls_folders = get_urls_folders(id)

    with Pool() as pool:
        pool.map(download_file_helper, urls_folders)

