"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean

# Testing FOR Errors
import pytest
from inflammation.models import daily_min
...
def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])
# End of testing FOR errors

# Unit 2 exercise to test the 1. daily_max() and 2. daily_min()

# Unit test exercise 1
def test_daily_max_integers():
    """Test that max function works for an array of positive integers."""
    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([5, 6])
npt.assert_array_equal(daily_max(data=test_input), test_result)

# Unit test exercise 2
def test_daily_min_integers():
    """Test that min function works for an array of positive and negative integers."""
    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6],
                           [-1, -2],
                           [-3, -4],
                           [-5, -6]])
    test_result = np.array([-5, -6])
npt.assert_array_equal(daily_min(data=test_input), test_result)

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(data=test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

