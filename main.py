import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve

def integrate_linear_function(slope, intercept, x_start, x_end):
    """Creates a linear function y = mx + c over a range.
    Args:
        slope (float): Slope of the linear function 
        intercept (float): Intercept of the linear function
        x_start (float): The starting x-value of the range.
        x_end (float): The ending x-value of the range.
    Returns:
        float: Value
    """
    def linear_function(x):
        return slope * x + intercept
    result, _ = quad(linear_function, x_start, x_end)
    return result


def solve_system_of_equations(a1, b1, c1, a2, b2, c2):
    """Solves 2 linear equations
        a1*x + b1*y = c1
        a2*x + b2*y = c2
    Args:
        a1, b1, c1 (float): Coefficients 1 quation.
        a2, b2, c2 (float): Coefficients 2 equation.
    Returns:
        dict: A dictionary with keys 'X' and 'Y' 
    """
    coefficients = np.array([[a1, b1], [a2, b2]])
    constants = np.array([c1, c2])
    solution = solve(coefficients, constants)
    return {'X': solution[0], 'Y': solution[1]}

