import requests, logging
from bs4 import BeautifulSoup

url = "https://links.sgx.com/1.0.0/derivatives-historical/5380/TC_structure.dat"
# Check if data is available before downloading it
def check():
    response = requests.post(url)

    if "No Record Found" in response.text:
        logging.error("No Record Found")
        return

check()