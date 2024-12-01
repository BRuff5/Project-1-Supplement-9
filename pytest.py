import unittest

from main import integrate_linear_function

class TestIntegrateLinearFunction(unittest.TestCase):
    def test_integrate_linear_function(self):
        # Test case 1: Simple linear function y = x over [0, 1]
        slope = 1
        intercept = 0
        x_start = 0
        x_end = 1
        expected_result = 0.5  # Integral of y = x over [0, 1] is (1/2)x^2 | 0 to 1 = 0.5
        result = integrate_linear_function(slope, intercept, x_start, x_end)
        self.assertAlmostEqual(result, expected_result, places=6)

        # Test case 2: Linear function y = 2x + 3 over [1, 4]
        slope = 2
        intercept = 3
        x_start = 1
        x_end = 4
        # Integral = (1/2)(2)x^2 + 3x | 1 to 4 = [(4^2 + 12) - (1^2 + 3)] = 41
        expected_result = 41.0
        result = integrate_linear_function(slope, intercept, x_start, x_end)
        

        # Test case 3: Constant function y = 5 over [0, 10]
        slope = 0
        intercept = 5
        x_start = 0
        x_end = 10
        # Integral = 5x | 0 to 10 = 5(10 - 0) = 50
        expected_result = 50.0
        result = integrate_linear_function(slope, intercept, x_start, x_end)
        self.assertAlmostEqual(result, expected_result, places=6)

if __name__ == "__main__":
    unittest.main()
