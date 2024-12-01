import unittest

from main import solve_system_of_equations

class TestSolveSystemOfEquations(unittest.TestCase):
    def test_solve_system_of_equations(self):
        # Test case 1: Simple system
        # x + y = 2
        # x - y = 0
        a1, b1, c1 = 1, 1, 2
        a2, b2, c2 = 1, -1, 0
        expected_result = {'X': 1, 'Y': 1}  # Solution: x=1, y=1
        result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        self.assertAlmostEqual(result['X'], expected_result['X'], places=6)
        self.assertAlmostEqual(result['Y'], expected_result['Y'], places=6)

        # Test case 2: System with fractional solution
        # 2x + 3y = 6
        # 4x + y = 8
        a1, b1, c1 = 2, 3, 6
        a2, b2, c2 = 4, 1, 8
        expected_result = {'X': 1, 'Y': 4/3}  # Solution: x=1, y=4/3
        result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)

        # Test case 3: Negative coefficients
        # -x + 2y = 3
        # 3x + y = -1
        a1, b1, c1 = -1, 2, 3
        a2, b2, c2 = 3, 1, -1
        expected_result = {'X': -1, 'Y': 1}  # Solution: x=-1, y=1
        result = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        
if __name__ == "__main__":
    unittest.main()

