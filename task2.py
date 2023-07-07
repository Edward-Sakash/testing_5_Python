"""
# Exercise 2 (Testing an Exception):
Write a pytest test case to verify that the following function raises
a ValueError exception when the input is zero:
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
import pytest

def test_divide_numbers():
    with pytest.raises(ValueError):
        _________(10, ____)
            
"""

# Solution
import pytest

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_numbers():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)
