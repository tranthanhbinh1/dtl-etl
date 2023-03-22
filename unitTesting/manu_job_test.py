import unittest
from unittest.mock import patch

class TestDownloadFile(unittest.TestCase):
    
    @patch("wget.download")
    @patch("logging.Logger.error")
    @patch("logging.Logger.info")
    @patch("requests.post")
    def test_download_file(self, mock_post, mock_info, mock_error, mock_download):
        from crawler.manu_job import download_file  # Import the function from your script
        
        # Test when no records are found
        url = "https://links.sgx.com/1.0.0/derivatives-historical/6000/WEBPXTICK_DT.zip"
        destination_folder = "data"
        mock_post.return_value.text = "No Record Found"
        
        download_file(url, destination_folder)
        
        self.assertTrue(mock_error.called)
        self.assertEqual(mock_error.call_args[0][0], "No Record Found")
        
        # Test when records are found and download is successful
        url = "https://links.sgx.com/1.0.0/derivatives-historical/5375/WEBPXTICK_DT.zip"
        destination_folder = "data"
        mock_post.return_value.text = "Records Found"
        
        download_file(url, destination_folder)
        
        self.assertTrue(mock_info.called)
        self.assertEqual(mock_info.call_args[0][0], f"Successfully downloaded {url}")
        
        # Test when records are found but an error occurs during download
        url = "https://links.sgx.com/1.0.0/derivatives-historical/5375/WEBPXTICK_DT.zip"
        destination_folder = "data"
        mock_post.return_value.text = "Records Found"
        
        def side_effect(*args):
            raise Exception("Download error")
        
        mock_download.side_effect = side_effect
    
        download_file(url, destination_folder)
        
        self.assertTrue(mock_error.called)
        self.assertEqual(mock_error.call_args[0][0], f"Error downloading {url}: Download error")

if __name__ == "__main__":
   unittest.main()