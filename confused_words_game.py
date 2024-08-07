import random


class ConfusedWordsGame:
    """
        Игра 'Перепутанные слова'.
        Игроку дается список слов с переставленными буквами, которые необходимо восстановить.
    """

    def __init__(self):
        # Список правильных слов
        self.words = [
            'программа',
            'игра',
            'перепутать',
            'торт',
            'компьютер',
        ]

    def shuffle_word(self, word: str) -> str:
        """
            Метод для перемешивания символов в слове.
        """
        word = list(word)
        random.shuffle(word)
        return ''.join(word)

    def main_logic_game(self) -> None:
        """
            Основная логика игры
        """
        # Создаем список "Перепутанных слов"
        shuffled_words = [self.shuffle_word(word) for word in self.words]

        while True:
            correct_count = 0
            for original_word, shuffled_word in zip(self.words, shuffled_words):
                print(f"Перепутанное слово: {shuffled_word}")
                guess = input("Ваш ответ: ").strip().lower()
                if guess == "exit":
                    print("Спасибо за игру!")
                    exit()
                elif guess == original_word:
                    print("Верно!")
                    correct_count += 1
                else:
                    print(f"Неправильно. Правильный ответ: {original_word}")
            print(f"Вы угадали {correct_count} из {len(self.words)} слов.")
            play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
            if play_again != "да":
                print("Спасибо за игру!")
                break
            else:
                shuffled_words = [self.shuffle_word(word) for word in self.words]

    def start_game(self) -> None:
        """
            Приветственное сообщение при запуске игры и ее правила
        """
        print("Добро пожаловать в игру 'Перепутанные слова'!")
        print("Угадайте правильные слова из перепутанных букв.")
        print("Для завершения игры введите 'exit'.")
        self.main_logic_game()


if __name__ == '__main__':
    game = ConfusedWordsGame()
    game.start_game()
