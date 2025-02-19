"""
Basic Calculator Fuctions - Addition, Subtraction, Multiplication, and Division
"""

# Remove unused imports
# from calculator.operations import subtract, multiply  # DELETE if not used
import pytest  # KEEP only if it's used in the file
from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Returns the sum of x and y."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Returns the difference of x and y."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Returns the product of x and y."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
