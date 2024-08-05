class IntToHex:
    """
        Класс преобразования целого числа из десятичной системы счисления в шестнадцатеричную.
    """

    def __init__(self):
        self.hex_map = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F',
        }

    def int_to_hex(self, num: int) -> str:
        """
            Метод преобразования целого числа из десятичной системы счисления в шестнадцатеричную
        """
        if num == 0:
            return '0x0'

        hex_digits = []
        while num > 0:
            remainder = num % 16
            if remainder >= 10:
                hex_digits.append(self.hex_map[remainder])
            else:
                hex_digits.append(str(remainder))
            num //= 16

        hex_digits.reverse()
        return '0x' + ''.join(hex_digits)


if __name__ == '__main__':
    converter = IntToHex()
    int_to_hex = converter.int_to_hex(1000)
    print(int_to_hex)
