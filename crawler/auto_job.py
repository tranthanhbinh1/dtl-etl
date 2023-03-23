import wget, os
from multiprocessing import Pool
from config.default import get_urls_folders, base_id
from utils.utils import (create_folder, current_path, file_logger, download_file_helper, 
                         check_data_available, get_last_id, save_last_id)


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
    get_last_id()
    
    last_id = get_last_id()
    if last_id is None:
        # First run, use base id
        id = base_id
    else:
        # Increment last id by 1
        id = last_id + 1
    # If the Id is valid, save the current id for next run
    if check_data_available(get_urls_folders(id)[0][0]):
        save_last_id(id)

    urls_folders = get_urls_folders(id)

    with Pool() as pool:
        pool.map(download_file_helper, urls_folders)

