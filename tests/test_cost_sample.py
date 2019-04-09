import unittest
from solver.cost_sample import cost_function

class TestCostFunction(unittest.TestCase):

    def test_exact_value(self):
        self.assertEqual(cost_function(1,2,3), 1)

    def test_round_value(self):
        self.assertEqual(cost_function(2,3,3), 1)

if __name__ == '__main__':
    unittest.main()