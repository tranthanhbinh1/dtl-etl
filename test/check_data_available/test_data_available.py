import unittest
from unittest.mock import patch

class TestCheckDataAvailable(unittest.TestCase):
    @patch("requests.get")
    def test_check_data_available(self, mock_get):
        from utils.utils import check_data_available  # Import the function from your script
        
        # Test when "No Record Found" is in the response text
        url = "https://links.sgx.com/1.0.0/derivatives-historical/6000/WEBPXTICK_DT.zip"
        mock_response = unittest.mock.Mock()
        mock_response.text = "No Record Found"
        mock_get.return_value = mock_response
        
        result = check_data_available(url)
        
        self.assertFalse(result)
        
        # Test when "No Record Found" is not in the response text
        url = "https://links.sgx.com/1.0.0/derivatives-historical/5375/WEBPXTICK_DT.zip"
        mock_response = unittest.mock.Mock()
        mock_response.text = "Record Found"
        mock_get.return_value = mock_response
        
        result = check_data_available(url)
        
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()