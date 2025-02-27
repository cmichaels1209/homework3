"""
Basic Calculator Fuctions - Addition, Subtraction, Multiplication, and Division
"""
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
