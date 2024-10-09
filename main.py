from addition_subtraction import AdditionSubtraction
from multiplication_division import MultiplicationDivision
from power_root import PowerRoot

def get_numbers():
    """Функция для получения двух чисел от пользователя."""
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return a, b

def main():
    # Создание экземпляров классов
    calc_add_sub = AdditionSubtraction()
    calc_mul_div = MultiplicationDivision()
    calc_pow_root = PowerRoot()
