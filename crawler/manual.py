import wget, os, sys
from multiprocessing import Pool
from utils.utils import current_path, create_folder
from config.default import get_urls_folders


def download_file(args):
    url, destination_folder = args
    destination_path = os.path.join(current_path, destination_folder)
    wget.download(url, out=destination_path)
    

if __name__ == "__main__":
    create_folder()

    if len(sys.argv) < 2:
        print("Usage: python -m crawler.test [id]")
        sys.exit(1)

    id = sys.argv[1]

    urls_folders = get_urls_folders(id)

    with Pool() as pool:
        pool.map(download_file, urls_folders)




