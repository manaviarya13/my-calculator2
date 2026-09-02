"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""

import pytest
from src.calculator import add, divide, subtract, multiply, power, square_root


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6


class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""

    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)

        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


class TestPower:
    """Test power operation."""

    def test_power_positive_numbers(self):
        """Test raising a number to a positive power."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero(self):
        """Test raising a number to the power of zero."""
        assert power(10, 0) == 1

    def test_power_input_validation(self):
        """Test power rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power("2", 3)

        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power(2, "3")


class TestSquareRoot:
    """Test square root operation."""

    def test_square_root_positive_number(self):
        """Test square root of a positive number."""
        assert square_root(16) == 4
        assert square_root(25) == 5

    def test_square_root_zero(self):
        """Test square root of zero."""
        assert square_root(0) == 0

    def test_square_root_input_validation(self):
        """Test square root rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Argument must be a number"):
            square_root("16")

    def test_square_root_negative_number(self):
        """Test square root rejects negative numbers."""
        with pytest.raises(ValueError, match="negative numbers are not allowed"):
            square_root(-16)


# TODO: Students will add more tests