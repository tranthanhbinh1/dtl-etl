import unittest
from crawler.manu_job import download_file

class testManuJob(unittest.TestCase):

    def test_downloadFile(self):
        result = download_file("https://links.sgx.com/1.0.0/derivatives-historical//WEBPXTICK_DT.zip")