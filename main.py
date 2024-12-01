import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve

def integrate_linear_function(slope, intercept, x_start, x_end):
    """
    Integrates a linear function y = mx + c over a specified range [x_start, x_end].
    
    Args:
        slope (float): The slope of the linear function (m).
        intercept (float): The intercept of the linear function (c).
        x_start (float): The starting x-value of the range.
        x_end (float): The ending x-value of the range.
        
    Returns:
        float: The definite integral value over the range.
    """
    def linear_function(x):
        return slope * x + intercept
    
    result, _ = quad(linear_function, x_start, x_end)
    return result


def solve_system_of_equations(a1, b1, c1, a2, b2, c2):
    """
    Solves a system of two linear equations of the form:
        a1*x + b1*y = c1
        a2*x + b2*y = c2
    
    Args:
        a1, b1, c1 (float): Coefficients of the first equation.
        a2, b2, c2 (float): Coefficients of the second equation.
        
    Returns:
        dict: A dictionary with keys 'X' and 'Y' representing the solution.
    """
    coefficients = np.array([[a1, b1], [a2, b2]])
    constants = np.array([c1, c2])
    solution = solve(coefficients, constants)
    return {'X': solution[0], 'Y': solution[1]}


def generate_normal_samples(n_samples, mean, std_dev):
    """
    Generates a specified number of samples from a normal distribution.
    
    Args:
        n_samples (int): Number of samples to generate.
        mean (float): Mean of the distribution.
        std_dev (float): Standard deviation of the distribution.
        
    Returns:
        np.ndarray: An array of generated samples.
    """
    return np.random.normal(mean, std_dev, n_samples)


# Example usage:
if __name__ == "__main__":
    # Integrate a linear function
    slope = 2
    intercept = 3
    x_start = 0
    x_end = 5
    integral_result = integrate_linear_function(slope, intercept, x_start, x_end)
    print(f"Integral result: {integral_result}")

    # Solve a system of equations
    a1, b1, c1 = 1, 2, 9  # Equation 1: x + 2y = 9
    a2, b2, c2 = 3, -4, 1  # Equation 2: 3x - 4y = 1
    solution = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
    print(f"Solution to the system: {solution}")

    # Generate samples from a normal distribution
    n_samples = 10
    mean = 0
    std_dev = 1
    samples = generate_normal_samples(n_samples, mean, std_dev)
    print(f"Generated samples: {samples}")
