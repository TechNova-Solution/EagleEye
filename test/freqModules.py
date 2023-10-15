import unittest
import os
from freqModules import allowed_file, file_to_list

class TestFileFunctions(unittest.TestCase):

    def test_allowed_file(self):
        # Test with valid file extensions
        valid_extensions = ['.csv', 'data.csv', 'file.CSV']
        for ext in valid_extensions:
            self.assertTrue(allowed_file(ext), f"Expected {ext} to be allowed")

        # Test with invalid file extensions
        invalid_extensions = ['.txt', 'image.jpg', 'file.pdf']
        for ext in invalid_extensions:
            self.assertFalse(allowed_file(ext), f"Expected {ext} to be disallowed")

    def test_file_to_list(self):
        # Create a temporary CSV file for testing
        with open('test_file.csv', 'w') as file:
            file.write('1,2,3,4,5')

        # Test file_to_list function
        result = file_to_list('test_file.csv')
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected, "Expected file_to_list to return the correct list")

        # Clean up the temporary file
        os.remove('test_file.csv')

if __name__ == '__main__':
    unittest.main()
