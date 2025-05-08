"""Check some of the functions in arithmetic.
"""
import numpy as np
from arithmetic import square


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
    # Given
    x = 3.4
    y_theo = 11.56
    # When
    y = square(x)
    # Then
    assert np.isclose(y,y_theo)


# code to execute only if Python is executed directly on this module,
# NOT on import
if __name__ == '__main__':
    test_square_integer()
    test_square_float()






