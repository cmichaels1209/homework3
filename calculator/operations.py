"""
Basic Calculator Fuctions - Addition, Subtraction, Multiplication, and Division
"""

def add(a,b):
    """Returns the sum of x and y."""
    return a + b

def subtract(a,b):
    """Returns the difference of x and y."""
    return a - b

def multiply(a,b):
    """Returns the product of x and y."""
    return a * b

def divide(a,b):
    if b == 0: 
        raise ValueError("Error! Cannot Divide by Zero!") 
     return a / b 
