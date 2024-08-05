def arithmetic_operations(num1: int, num2: int) -> [int, int, int, int, int]:
    """
        Функция, выполняющая арифметические операции с целыми числами
    """
    sum_ = num1 + num2
    ded = num1 - num2
    mult = num1 * num2
    div = round(num1 / num2, 2)
    rem = num1 % num2
    return [sum_, ded, mult, div, rem]


if __name__ == "__main__":
    print('Арифметические операции с двумя числами')
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print(f'Cумма введенных чисел: {arithmetic_operations(num1, num2)[0]}')
    print(f'Разница введенных чисел: {arithmetic_operations(num1, num2)[1]}')
    print(f'Умножение введенных чисел: {arithmetic_operations(num1, num2)[2]}')
    print(f'Деление введенных чисел: {arithmetic_operations(num1, num2)[3]}')
    print(f'Остаток от деления введенных чисел: {arithmetic_operations(num1, num2)[4]}')
