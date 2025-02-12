from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a, b):
        calculation = Calculation(a, b, add)  """Pass the add function"""
        return calculation.get_result()

    @staticmethod
    def subtract(a, b):
        calculation = Calculation(a, b, subtract)  """Pass the subtract function"""
        return calculation.get_result()

    @staticmethod
    def multiply(a, b):
        calculation = Calculation(a, b, multiply)  """Pass the multiply function"""
        return calculation.get_result()

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        calculation = Calculation(a, b, divide)  """Pass the divide function"""
        return calculation.get_result()
