import wget, os, logging
from datetime import datetime, date
from multiprocessing import Pool
from utils.utils import create_folder, current_path

# Set up logging to write logs to a file
logging.basicConfig(filename='my_script.log', level=logging.INFO)

def get_id_from_date(base_id, start_date):
    # Get current date
    today = datetime.now()
    # Calculate days passed since start date
    days_passed = (today - start_date).days
    # Increment base id by days passed
    id = base_id + days_passed
    logging.info(f'Current id: {id}')
    return id

def download_file(args):
    url, destination_folder = args
    destination_path = os.path.join(current_path, destination_folder)
    try:
        wget.download(url, out=destination_path)
        logging.info(f'Successfully downloaded {url}')
    except Exception as e:
        logging.error(f'Error downloading {url}: {e}')
    
def get_urls_folders(id):
    return [
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/WEBPXTICK_DT.zip", "data/tick"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TickData_structure.dat", "data/tickDs"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TC.txt", "data/tradeCancel"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TC_structure.dat", "data/tradeCancelDs"),
    ]

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
