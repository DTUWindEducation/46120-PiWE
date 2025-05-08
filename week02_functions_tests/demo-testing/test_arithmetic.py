"""Check some of the functions in arithmetic.
"""
from arithmetic import square
import numpy as np


def test_square_integer():
    """Test that the square function returns the correct value for an
    integer input."""
    # given
    x = 2
    y_theo = 4
    # when
    y = square(x)
    # then
    assert y == y_theo

def test_square_float():
    """Test that the square function returns the correct value for a
    float input."""
    # given
    x_f = 3.4
    y_f_theo = 11.56
    # when
    y_f = square(x_f)
    # then
    assert np.isclose(y_f, y_f_theo)


# code to execute only if Python is executed directly on this module,
# NOT on import
if __name__ == '__main__':
    test_square_integer()
    test_square_float()
