from typing import List


class InvertedList:
    """
        Программа, которая переставляет в обратном порядке все элементы списка и подсчитывает длину списка.
    """

    def __init__(self):
        # Изначальный список
        self.list_items = [
            'программа',
            'игра',
            'перепутать',
            'торт',
            'компьютер',
        ]

    def flip_list(self, list_items: List[str]) -> List[str]:
        """
            Метод, возвращающий список с элементами первоначального списка в обратном порядке
        """
        return list(reversed(list_items))

    def counting_list_items(self, list_items: List[str]) -> int:
        """
            Метод, подсчитывающий количество элементов в списке
        """
        return len(list_items)

    def main_logic_program(self) -> None:
        """
            Логика программы
        """
        inverted_list = self.flip_list(self.list_items)
        inverted_list_len = self.counting_list_items(inverted_list)
        print(f"Изначальный список элементов: {self.list_items}")
        print(f"Список элементов в обратном порядке: {inverted_list}")
        print(f"Количество элементов в перевернутом списке: {inverted_list_len}")


if __name__ == '__main__':
    inv = InvertedList()
    inv.main_logic_program()
