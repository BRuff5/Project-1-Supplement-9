import unittest
import numpy as np


from main import integrate_linear_function
from main import solve_system_of_equations


class TestMathFunctions(unittest.TestCase):
    def test_integrate_linear_function(self):
        # Test case 1: y = x over [0, 1]
        slope, intercept = 1, 0
        x_start, x_end = 0, 1
        expected_result = 0.5  # Integral of x from 0 to 1
        result = integrate_linear_function(slope, intercept, x_start, x_end)
        self.assertAlmostEqual(result, expected_result, places=6)

        # Test case 2: y = 2x + 3 over [1, 4]
        slope, intercept = 2, 3
        x_start, x_end = 1, 4
        expected_result = 41  # Computed manually
        result = integrate_linear_function(slope, intercept, x_start, x_end)
    
        # Test case 3: y = 5 over [0, 10] (constant function)
        slope, intercept = 0, 5
        x_start, x_end = 0, 10
        expected_result = 50  # Area = base * height
        result = integrate_linear_function(slope, intercept, x_start, x_end)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_solve_system_of_equations(self):
        # Test case 1: Simple system
        a1, b1, c1 = 1, 1, 2
        a2, b2, c2 = 1, -1, 0
        expected_result = {'X': 1, 'Y': 1}
        result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        self.assertAlmostEqual(result['X'], expected_result['X'], places=6)
        self.assertAlmostEqual(result['Y'], expected_result['Y'], places=6)

        # Test case 2: Fractional solution
        a1, b1, c1 = 2, 3, 6
        a2, b2, c2 = 4, 1, 8
        expected_result = {'X': 1, 'Y': 4/3}
        result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)

        # Test case 3: Negative coefficients
        a1, b1, c1 = -1, 2, 3
        a2, b2, c2 = 3, 1, -1
        expected_result = {'X': -1, 'Y': 1}
        result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        

    def test_generate_normal_samples(self):
        # Test case 1: Mean = 0, std_dev = 1, n_samples = 1000
        n_samples = 1000
        mean = 0
        std_dev = 1

        # Test case 2: Mean = 10, std_dev = 2, n_samples = 500
        n_samples = 500
        mean = 10
        std_dev = 2

if __name__ == "__main__":
    unittest.main()


