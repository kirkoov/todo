import unittest

from calculator import MadCalculator


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    # def setUp(self):
    #     """Подготовка прогона теста. Вызывается перед каждым тестом."""
    #     # Arrange - подготавливаем данные для теста
    #     print("Calling the setUp(self)...")  # 4 times...
    #     self.calc = MadCalculator()

    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        # Arrange - подготавливаем данные для теста
        # print("Calling the setUp(self)...")  # 1 time only
        cls.calc = MadCalculator()

    # def test_sum_string(self):
    #     # sum_string() возвращает конкатенированные строки
    #     act = self.calc.sum_string(1, 100500)
    #     self.assertEqual(act, 1100500, 'Метод sum_string работает неправильно.')
    def test_sum_string(self):
        act = TestCalc.calc.sum_string(1, 100500)
        self.assertEqual(act, 1100500, 'Метод sum_string работает неправильно.')

    # def test_sum_string_first_negative_value(self):
    #     # Проверяем, что при вызове метода sum_string() с отрицательным числом
    #     # в аргументе выбрасывается исключение ValueError
    #     self.assertRaises(ValueError, self.calc.sum_string, -1, 100500)
    def test_sum_string_first_negative_value(self):
        self.assertRaises(ValueError, TestCalc.calc.sum_string, -1, 100500)

    # def test_sum_string_second_negative_value(self):
    #     # Можно провести тестирование исключения,
    #     # использовав менеджер контекста
    #     with self.assertRaises(ValueError):
    #         self.calc.sum_string(1, -100500)
    def test_sum_string_second_negative_value(self):
        with self.assertRaises(ValueError):
            TestCalc.calc.sum_string(1, -100500)

    # def test_sum_args(self):
    #     # sum_args возвращает сумму принятых аргументов

    #     # Act - выполнение тестируемого сценария.
    #     # Вызываем метод sum
    #     act = self.calc.sum_args(3, -3, 5)

    #     # Assert - проверяем, что метод работает
    #     self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')

    def test_sum_args(self):
        act = TestCalc.calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')


if __name__ == "__main__":
    unittest.main()
