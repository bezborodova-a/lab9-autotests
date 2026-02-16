class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def is_prime(self, n):
        if n <= 0:
            raise ValueError("Number must be positive!")
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    def power(self, base, exponent):
        return base ** exponent