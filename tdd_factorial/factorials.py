"""
importing the math library
"""
import math


class Factorial:

    """
    the class is finding the factorial of  number
    """

    def __init__(self, num_n):
        self.num_n = num_n

    def factorials(self):
        """
        the function is finding the factorial of the number
        """

        return math.factorial(self.num_n)
        # num = 1
        # for i in range(self.n, 0,  -1):
        #     num = num * i
        #     print(num)
