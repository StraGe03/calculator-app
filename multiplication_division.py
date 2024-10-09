# multiplication_division.py
class MultiplicationDivision:
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль!"
