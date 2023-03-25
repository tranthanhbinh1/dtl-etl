import wget, os, sys
from datetime import datetime
from multiprocessing import Pool
from utils.utils import (current_path, create_folder, file_logger, calculate_id,
                         console_logger, download_file_helper, check_data_available)
from config.default import get_urls_folders, base_id


def download_file(url, destination_folder):
    # Check if the records are available
    if check_data_available(url) == False:
        console_logger.error("No Record Found")
        return
    destination_path = os.path.join(current_path, destination_folder)
    try:
        wget.download(url, out=destination_path)
        file_logger.info(f'Successfully downloaded {url}')
        console_logger.info(f'Successfully downloaded {url}')
    except Exception as e:
        file_logger.error(f'Error downloading {url}: {e}')
        console_logger.error(f'Error downloading {url}: {e}')


if __name__ == "__main__":
    create_folder()

    if len(sys.argv) < 2:
        print("Command: python -m crawler.test [date] [optional: link_index]")
        sys.exit(1)

    date_str = sys.argv[1]
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    urls_folders = get_urls_folders(calculate_id(date, base_id))
    
    if len(sys.argv) >= 3:
        link_index = int(sys.argv[2])
        if link_index < 0 or link_index >= len(urls_folders):
            print(f"Invalid link index: {link_index}. Must be between 0 and {len(urls_folders)-1}")
            sys.exit(1)
        urls_folders = [urls_folders[link_index]]

    file_logger.info(f"Manually download with {id} and link index {link_index if len(sys.argv) >= 3 else 'all'}")
    
    with Pool() as pool:
        pool.map(download_file_helper, urls_folders)



