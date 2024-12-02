import unittest
import numpy as np

from main import integrate_linear_function, solve_system_of_equations

class TestMathFunctions(unittest.TestCase):
    def test_integrate_linear_function(self):
        # Test case 1: y = 2x + 3 over [0, 5]
        slope = 2
        intercept = 3
        x_start = 0
        x_end = 5
        expected_result = 55  # Manually computed: integral = (2/2)x^2 + 3x | 0 to 5 = 55
        result = integrate_linear_function(slope, intercept, x_start, x_end)

        # Test case 2: y = -x + 1 over [0, 3]
        slope = -1
        intercept = 1
        x_start = 0
        x_end = 3
        expected_result = -3  # Manually computed
        result = integrate_linear_function(slope, intercept, x_start, x_end)

    def test_solve_system_of_equations(self):
        # Test case 1: x + 2y = 9, 3x - 4y = 1
        a1, b1, c1 = 1, 2, 9
        a2, b2, c2 = 3, -4, 1
        expected_result = {'X': 5, 'Y': 2}  # Manually solved
        result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)

        # Test case 2: 2x + 3y = 6, 4x - y = 5
        a1, b1, c1 = 2, 3, 6
        a2, b2, c2 = 4, -1, 5
        expected_result = {'X': 2, 'Y': 0}  # Manually solved
        result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        

    def test_generate_normal_samples(self):
        # Test case 1: Generate 1000 samples from N(0, 1)
        n_samples = 1000
        mean = 0
        std_dev = 1
        

        # Test case 2: Generate 500 samples from N(10, 2)
        n_samples = 500
        mean = 10
        std_dev = 2
        

if __name__ == "__main__":
    unittest.main()
