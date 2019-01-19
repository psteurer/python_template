import unittest


class TestMain(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.input = [1, 2, 3]
        self.result = 6

    def test_sum(self):
        self.assertEqual(sum(self.input), self.result, "Should be 6")


if __name__ == '__main__':
    unittest.main()
