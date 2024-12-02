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

def generate_normal_samples(n_samples, mean, std_dev):
    """Generates a specified number
    Args:
        n_samples (int): Number 
        mean (float): Mean 
        std_dev (float): Standard deviation 
    Returns:
        array: array
    """
    return np.random.normal(mean, std_dev, n_samples)

if __name__ == "__main__":
    """Linear function"""
    slope = 2
    intercept = 3
    x_start = 0
    x_end = 5
    integral_result = integrate_linear_function(slope, intercept, x_start, x_end)
    print(f"Linear Function: y = {slope}x + {intercept} from x = {x_start} to x = {x_end}: {integral_result}")

    """Solve Equations"""
    a1, b1, c1 = 1, 2, 9  # Equation 1: x + 2y = 9
    a2, b2, c2 = 3, -4, 1  # Equation 2: 3x - 4y = 1
    solution = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
    print(f"x + 2y = 9 and 3x - 4y = 1: {solution}")


    n_samples = 10
    mean = 0
    std_dev = 1
    samples = generate_normal_samples(n_samples, mean, std_dev)
    print(f"Generated {n_samples} from a mean: ({mean}, {std_dev}^2) distribution: {samples}")