import wget, os, sys, requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from utils.utils import current_path, create_folder, file_logger, console_logger
from config.default import get_urls_folders


def download_file(args):
    url, destination_folder = args
    # Check if the records are available
    response = requests.post(url)
    if "No Record Found" in response.text:
        console_logger.error("No Record Found")
        return
    destination_path = os.path.join(current_path, destination_folder)
    try:
        wget.download(url, out=destination_path)
        file_logger.info(f'Successfully downloaded {url}')
    except Exception as e:
        file_logger.error(f'Error downloading {url}: {e}')


if __name__ == "__main__":
    create_folder()

    if len(sys.argv) < 2:
        print("Command: python -m crawler.test [id] [optional: link_index]")
        sys.exit(1)

    id = sys.argv[1]
    
    urls_folders = get_urls_folders(id)
    
    if len(sys.argv) >= 3:
        link_index = int(sys.argv[2])
        
        if link_index < 0 or link_index >= len(urls_folders):
            print(f"Invalid link index: {link_index}. Must be between 0 and {len(urls_folders)-1}")
            sys.exit(1)

        urls_folders = [urls_folders[link_index]]
    
    file_logger.info(f"Manually download with {id} and link index {link_index if len(sys.argv) >= 3 else 'all'}")
    
    with Pool() as pool:
        pool.map(download_file, urls_folders)


