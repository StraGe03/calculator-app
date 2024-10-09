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

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Извлечение корня")
        print("7. Выход")

        choice = input("Введите номер операции (1-7): ")

        if choice == '1':
            a, b = get_numbers()
            print(f"Результат сложения: {calc_add_sub.add(a, b)}")
        
        elif choice == '2':
            a, b = get_numbers()
            print(f"Результат вычитания: {calc_add_sub.subtract(a, b)}")
        
        elif choice == '3':
            a, b = get_numbers()
            print(f"Результат умножения: {calc_mul_div.multiply(a, b)}")
        
        elif choice == '4':
            a, b = get_numbers()
            print(f"Результат деления: {calc_mul_div.divide(a, b)}")
        
        elif choice == '5':
            a, b = get_numbers()
            print(f"Результат возведения в степень: {calc_pow_root.power(a, b)}")
        
        elif choice == '6':
            a, b = get_numbers()
            print(f"Результат извлечения корня: {calc_pow_root.root(a, b)}")
        
        elif choice == '7':
            print("Программа завершена.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if name == "__main__":
    main()
