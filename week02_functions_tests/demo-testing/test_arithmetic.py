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
    """ Test tha the input is a float"""
    # given
    x = 3.4
    y_theo = 11.56
    # when
    y = square(x)
    # then
    assert np.isclose(y, y_theo)


# code to execute only if Python is executed directly on this module,
# NOT on import
if __name__ == '__main__':
    test_square_float()
