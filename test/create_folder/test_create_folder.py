from unittest.mock import patch
import os

@patch("os.makedirs")
def test_create_folder(mock_makedirs):
    from utils.utils import create_folder  # Import the function from your script
    
    # Call the function
    create_folder()
    
    # Check that os.makedirs was called with the expected arguments
    expected_calls = [
        ((os.path.join("data", "tick"),),),
        ((os.path.join("data", "tickDs"),),),
        ((os.path.join("data", "tradeCancel"),),),
        ((os.path.join("data", "tradeCancelDs"),),),
    ]
    assert mock_makedirs.call_args_list == expected_calls