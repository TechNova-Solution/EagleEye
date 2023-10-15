import unittest
import generate

class TestGenerateFunction(unittest.TestCase):
    def test_generate_valid_range(self):
        result = generate(50, 10, 100)
        for value in result:
            self.assertTrue(10 <= value <= 50)  # Check if values are within the specified range

    def test_generate_population(self):
        result = generate(50, 10, 100)
        population_counts = [result.count(i) for i in range(1, 10)]
        expected_counts = [int(p * 100) for p in [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]]

        for expected, actual in zip(expected_counts, population_counts):
            self.assertAlmostEqual(expected, actual, delta=5)  # Check if generated population matches Benford's law

if __name__ == '__main__':
    unittest.main()
