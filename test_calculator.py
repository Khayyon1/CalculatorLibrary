'''
Unit tests for the calculator library
'''


from calculator import add, subtract, multiply, divide


class TestCalculator:
    """
    Testing simple calculator functions and showing convience of CI
    """
    def test_addition(self):
        assert 4 == add(2, 2)

    def test_subtraction(self):
        assert 2 == subtract(4, 2)

    def test_multiplication(self):
        assert 90 == multiply(10, 9)

    def test_division(self):
        assert 1 == divide(1, 1)
