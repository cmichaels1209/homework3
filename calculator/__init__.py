from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a, b):
        """Pass the add function"""
        calculation = Calculation(a, b, add)
        return calculation.get_result()

    @staticmethod
    def subtract(a, b):
        """Pass the subtract function"""
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(a, b):
        """Pass the multiply function"""
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        """Pass the divide function"""
        calculation = Calculation(a, b, divide)
        return calculation.get_result()

