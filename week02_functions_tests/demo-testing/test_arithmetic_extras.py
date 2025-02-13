"""Check some of the functions in arithmetic.
"""
from arithmetic import square
import numpy as np
from pytest import raises


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
    """Test that the square function returns the correct value for an
    integer input."""
    # given
    x = 3.4
    y_theo = 11.56
    # when
    y = square(x)
    # then
    assert np.isclose(y, y_theo)


def test_square_stringin():
    """Test an error is raised if a string is passed in."""
    # given
    x = 'cat'
    # when and then
    with raises(TypeError):  # assert a TypeError is raised
        square(x)


# code to execute only if Python is executed directly on this module,
# NOT on import
if __name__ == '__main__':
    test_square_integer()
    test_square_float()
    test_square_stringin()
