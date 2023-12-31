#!/usr/bin/python3
"""
This module shall multiply 2 matrix using the module NumPy
Return:
It shall return the muled matrix
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function multiplies 2 matrices by using the module NumPy
    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Returns:
        new matrix
    """
    return np.matmul(m_a, m_b)
