#My Calculator Test
from calculator.operations import add, multiply, subtract, divide
import pytest   #import pytest for exception testing

def test_addition():
    #Test addition function   
    assert add(2,2) == 4

def test_subtraction():
    #Test subtraction function  
    assert subtract(2,2) == 0

def test_multiplication():
    #Test that multiplication function
    assert multiply(2,2) == 4

def test_division():
    #Test division function
    assert divide(2,2) == 1

def test_division_by_zero():
    #Test division by zero raises an exception
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(2, 0) 
