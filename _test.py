import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

def test_square():
    assert square(2) == 4, " Test failed: Square of 2 should be 4"
    assert square(3) == 9, " Test failed: Square of 3 should be 9"

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")