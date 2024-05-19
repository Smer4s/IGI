import numpy as np

def init_matrix(rows: int, cols: int):
    """
    This method inits matrix with size rows*cols
    """
    return np.random.randint(0, 100, size=(rows, cols))

def get_side_diag(matrix):
    """This method returns side diagonal from matrix"""
    return np.diag(np.fliplr(matrix))

def min_elem_side_diag(matrix):
    """
    This method finds the smallest element on the side diagonal of a 2d matrix
    """
    return np.min(get_side_diag(matrix))



def std_var(matrix):
    """
    This method finds the dispersion of the side diagonal using standard numpy function
    """
    return np.var(get_side_diag(matrix))

def my_var(matrix):
    """
    This method finds the dispersion of the side diagonal using calculus
    """
    diagonal_elements = get_side_diag(matrix)
    mean = np.mean(diagonal_elements)
    variance_formula = np.mean((diagonal_elements - mean) ** 2)
    
    return variance_formula