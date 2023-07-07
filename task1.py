"""
Write a pytest test case to verify the correctness of the following
function that adds two numbers:
def add_numbers(a, b):
    return a + b


def test_add_numbers():
    assert __________(2, 3) == 5
    assert add_numbers(__, 1) == 0
    assert add_numbers(0, __) == 0
"""

# Solution

def add_numbers(a, b):
    return a + b


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-2, 3) == 1
    assert add_numbers(0, 0) == 0
