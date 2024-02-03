#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        A new matrix representing the product of m_a and m_b.
    """
    return np.dot(m_a, m_b)
