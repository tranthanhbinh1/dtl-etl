import wget, os, requests
from datetime import datetime, date
from multiprocessing import Pool
from config.default import get_urls_folders
from utils.utils import create_folder, current_path, file_logger


def get_id_from_date(base_id, start_date):
    # Get current date
    today = datetime.now()
    # Calculate days passed since start date
    days_passed = (today - start_date).days
    # Increment base id by days passed
    id = base_id + days_passed
    file_logger.info(f'Current id: {id}')
    return id

def download_file(url, destination_folder):
    response = requests.post(url)
    if "No Record Found" in response.text:
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

    # Set base id and start date
    base_id = 5379
    start_date = datetime(2023, 3, 20)

    # Get id from current date and base id
    id = get_id_from_date(base_id, start_date)

    urls_folders = get_urls_folders(id)

    with Pool() as pool:
        pool.map(download_file, urls_folders)
