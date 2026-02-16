

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """
    Класс тестов для Calculator.
    Каждый метод, начинающийся с 'test_', будет автоматически выполняться.
    """
    
    def setUp(self):
        """Метод, который выполняется ПЕРЕД каждым тестом"""
        self.calc = Calculator()
        print(f"\n Настройка для теста: {self._testMethodName}")
    
    def tearDown(self):
        """Метод, который выполняется ПОСЛЕ каждого теста"""
        print(f" Завершение теста: {self._testMethodName}\n")
    

    
    def test_add_positive_numbers(self):
        """Тест сложения положительных чисел"""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        print(f" test_add_positive_numbers: 2 + 3 = {result}")
    
    def test_add_negative_numbers(self):
        """Тест сложения отрицательных чисел"""
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)
        print(f" test_add_negative_numbers: -5 + (-3) = {result}")
    
    def test_add_mixed_numbers(self):
        """Тест сложения положительного и отрицательного чисел"""
        result = self.calc.add(10, -4)
        self.assertEqual(result, 6)
        print(f" test_add_mixed_numbers: 10 + (-4) = {result}")
    
 
    
    def test_subtract_numbers(self):
        """Тест вычитания"""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)
        print(f" test_subtract_numbers: 10 - 4 = {result}")
    
    def test_subtract_negative_result(self):
        """Тест вычитания с отрицательным результатом"""
        result = self.calc.subtract(3, 10)
        self.assertEqual(result, -7)
        print(f" test_subtract_negative_result: 3 - 10 = {result}")
    

    
    def test_multiply_positive(self):
        """Тест умножения положительных чисел"""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)
        print(f" test_multiply_positive: 3 * 4 = {result}")
    
    def test_multiply_by_zero(self):
        """Тест умножения на ноль"""
        result = self.calc.multiply(5, 0)
        self.assertEqual(result, 0)
        print(f" test_multiply_by_zero: 5 * 0 = {result}")
    

    
    def test_divide_normal(self):
        """Тест обычного деления"""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
        print(f" test_divide_normal: 10 / 2 = {result}")
    
    def test_divide_float_result(self):
        """Тест деления с дробным результатом"""
        result = self.calc.divide(5, 2)
        self.assertEqual(result, 2.5)
        print(f" test_divide_float_result: 5 / 2 = {result}")
    
    def test_divide_by_zero_raises_error(self):
        """
        Тест деления на ноль - должен вызывать исключение.
        Используем assertRaises для проверки исключений.
        """
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)
        

        self.assertEqual(str(context.exception), "Cannot divide by zero!")
        print(f" test_divide_by_zero_raises_error: Получена ошибка: {context.exception}")
    

    
    def test_is_prime_true(self):
        """Тест для простых чисел (должны возвращать True)"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for num in primes:
            with self.subTest(num=num):
                self.assertTrue(self.calc.is_prime(num))
        print(f" test_is_prime_true: Проверено {len(primes)} простых чисел")
    
    def test_is_prime_false(self):
        """Тест для составных чисел (должны возвращать False)"""
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15]
        for num in non_primes:
            with self.subTest(num=num):
                self.assertFalse(self.calc.is_prime(num))
        print(f" test_is_prime_false: Проверено {len(non_primes)} составных чисел")
    
    def test_is_prime_one(self):
        """Тест для числа 1 (не является простым)"""
        self.assertFalse(self.calc.is_prime(1))
        print(f" test_is_prime_one: 1 не является простым")
    
    def test_is_prime_negative_raises_error(self):
        """Тест для отрицательного числа - должен вызывать исключение"""
        with self.assertRaises(ValueError) as context:
            self.calc.is_prime(-5)
        
        self.assertEqual(str(context.exception), "Number must be positive!")
        print(f" test_is_prime_negative_raises_error: Получена ошибка: {context.exception}")
    
    
    
    def test_factorial_positive(self):
        """Тест факториала положительных чисел"""
        test_cases = [
            (0, 1),   # 0! = 1
            (1, 1),   # 1! = 1
            (2, 2),   # 2! = 2
            (3, 6),   # 3! = 6
            (4, 24),  # 4! = 24
            (5, 120)  # 5! = 120
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                result = self.calc.factorial(n)
                self.assertEqual(result, expected)
        
        print(f" test_factorial_positive: Проверено {len(test_cases)} значений факториала")
    
    def test_factorial_negative_raises_error(self):
        """Тест факториала отрицательного числа - должен вызывать исключение"""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(-1)
        
        self.assertEqual(str(context.exception), "Factorial is not defined for negative numbers!")
        print(f" test_factorial_negative_raises_error: Получена ошибка: {context.exception}")
    
   
    
    def test_power_positive_exponent(self):
        """Тест возведения в положительную степень"""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
        print(f" test_power_positive_exponent: 2^3 = {result}")
    
    def test_power_zero_exponent(self):
        """Тест возведения в нулевую степень (всегда 1)"""
        result = self.calc.power(5, 0)
        self.assertEqual(result, 1)
        print(f" test_power_zero_exponent: 5^0 = {result}")
    
    def test_power_negative_exponent(self):
        """Тест возведения в отрицательную степень"""
        result = self.calc.power(2, -2)
        self.assertEqual(result, 0.25)
        print(f" test_power_negative_exponent: 2^(-2) = {result}")
    
    def test_power_fractional_base(self):
        """Тест возведения дробного числа в степень"""
        result = self.calc.power(0.5, 2)
        self.assertEqual(result, 0.25)
        print(f" test_power_fractional_base: 0.5^2 = {result}")


class TestCalculatorParameterized(unittest.TestCase):
    """
    Дополнительные тесты с параметризацией.
    Показывает как тестировать один метод с разными наборами данных.
    """
    
    def setUp(self):
        self.calc = Calculator()
    
   
    def test_add_parameterized(self):
        """Параметризованный тест сложения"""
        test_cases = [
            (1, 2, 3),
            (-1, -2, -3),
            (0, 5, 5),
            (2.5, 2.5, 5.0),
            (-3, 3, 0)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                result = self.calc.add(a, b)
                self.assertEqual(result, expected)
        
        print(f" test_add_parameterized: Проверено {len(test_cases)} наборов данных")
    

    def test_divide_parameterized(self):
        """Параметризованный тест деления"""
        test_cases = [
            (10, 2, 5),
            (9, 3, 3),
            (1, 4, 0.25),
            (-10, 2, -5),
            (0, 5, 0)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                result = self.calc.divide(a, b)
                self.assertEqual(result, expected)
        
        print(f" test_divide_parameterized: Проверено {len(test_cases)} наборов данных")


if __name__ == '__main__':
    print(" ЗАПУСК МОДУЛЬНЫХ ТЕСТОВ (unittest)")
    print("=" * 60)
    

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCalculatorParameterized))
    

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
  
    print("\n" + "=" * 60)
    print(" СТАТИСТИКА ТЕСТОВ:")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    print("=" * 60)