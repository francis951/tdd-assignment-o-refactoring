"""
importing clas Fcatorial from the modue faactorial
"""
from factorials import Factorial


def test_factorial():
    """
    testing the factorial function
    """
    # Instantiate instance of a class
    answer = Factorial(4)
    # accessing the function
    assert answer.factorials() == 24

    answer = Factorial(6)
    # accessing the function
    assert answer.factorials() == 720

    answer = Factorial(8)
    # accessing the function
    assert answer.factorials() == 40320
