def function(x: int, y: int, z: int) -> int:
    """
        Функция решения линейного уравнения с тремя переменными
    """
    x = x
    y = y
    z = z
    res = x ^ 2 * (2 * y + 5 * z)
    return res


if __name__ == "__main__":
    x, y, z = map(int, input("Введите три числа через пробел: ").split())
    print(f'Результат вычисления: x^2 (2y + 5z) = {function(x, y, z)}')
