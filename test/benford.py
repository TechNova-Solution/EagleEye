import unittest

from benford import lead_digit_conter, leading_digit, benford_frequency, benford_percentages, benford_check, benford_data, benford_data_json, benford_data_csv

class TestBenfordFunctions(unittest.TestCase):

    def test_lead_digit_conter(self):
        leadData = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        lead_digit_conter(2, leadData)
        self.assertEqual(leadData, [0, 1, 0, 0, 0, 0, 0, 0, 0])

    def test_leading_digit(self):
        self.assertEqual(leading_digit(12345), 1)
        self.assertEqual(leading_digit(987.65), 9)
        self.assertIsNone(leading_digit(None))
        self.assertIsNone(leading_digit("abc"))

    def test_benford_frequency(self):
        values = [123, 456, 789, 111, 222, 333]
        leadData = benford_frequency(values)
        self.assertEqual(leadData, [1, 2, 3, 0, 0, 0, 0, 0, 0])

    def test_benford_percentages(self):
        leadData = [1, 2, 3, 0, 0, 0, 0, 0, 0]
        percentages = benford_percentages(leadData)
        self.assertEqual(percentages, [16.67, 33.33, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    def test_benford_check(self):
        percentages = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        self.assertTrue(benford_check(percentages))
        percentages[0] = 31.0  # Invalid value
        self.assertFalse(benford_check(percentages))

    def test_benford_data(self):
        leadData = [1, 2, 3, 0, 0, 0, 0, 0, 0]
        percentages = [16.67, 33.33, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        data = benford_data(percentages, leadData)
        self.assertEqual(data[0], [1, 16.67, 30.1, 13.43, 1])

    def test_benford_data_json(self):
        leadData = [1, 2, 3, 0, 0, 0, 0, 0, 0]
        percentages = [16.67, 33.33, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        data = benford_data_json(percentages, leadData)
        self.assertEqual(data['one']['count'], 1)
        self.assertEqual(data['two']['percentage'], 33.33)

    def test_benford_data_csv(self):
        leadData = [1, 2, 3, 0, 0, 0, 0, 0, 0]
        percentages = [16.67, 33.33, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        data = benford_data_csv(percentages, leadData)
        self.assertEqual(data, "1,16.67,30.1,13.43,2,33.33,17.6,16.27,3,50.0,12.5,37.5,0.0,0.0,9.7,-9.7,0.0,0.0,7.9,-7.9,0.0,0.0,6.7,-6.7,0.0,0.0,5.8,-5.8,0.0,0.0,5.1,-5.1,0.0,0.0,4.6,-4.6")

if __name__ == '__main__':
    unittest.main()
