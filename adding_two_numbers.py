def sum(num1: int, num2: int) -> int:
    """
        Функция сложения двух целых чисел
    """
    return num1 + num2


if __name__ == "__main__":
    print('Программа сложения двух чисел')
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print('Cумма введенных чисел: ', sum(num1, num2))
