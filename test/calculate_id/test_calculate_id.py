import unittest
from datetime import datetime
from workalendar.asia import Singapore
from utils.utils import calculate_id

class TestCalculateId(unittest.TestCase):
    def test_calculate_id(self):
        base_id = 1000
        date = datetime(2023, 3, 22)        #base date is 2023-03-20
        expected_id = 1002
        self.assertEqual(calculate_id(date, base_id), expected_id)

        date = datetime(2023, 3, 19)
        expected_id = 999
        self.assertEqual(calculate_id(date, base_id), expected_id)

if __name__ == '__main__':
    unittest.main()