# Excercise 1 (Testing a Simple Function):
Write a pytest test case to verify the correctness
of the following function that adds two numbers:
def add_numbers(a, b):
    return a + b


def test_add_numbers():
    assert __________(2, 3) == 5
    assert add_numbers(__, 1) == 0
    assert add_numbers(0, __) == 0

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