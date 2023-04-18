import unittest

from calculator import MadCalculator


def setUpModule():
    """Вызывается один раз перед всеми классами, которые есть в файле."""
    print('╭─setUpModule: called once EARLIEST b4 all classes in file')


def tearDownModule():
    """Вызывается один раз после всех классов, которые есть в файле."""
    print('╰─tearDownModule: called once LATEST after all classes in file')


class TestExample(unittest.TestCase):
    """Демонстрирует принцип работы тестов."""

    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        print('├──setUpClass: called once b4 all tests by this class')
        cls.calc = MadCalculator()

    @classmethod
    def tearDownClass(cls):
        """Вызывается один раз после запуска всех тестов класса."""
        print('\n├──tearDownClass: called once AFTER all tests by this class')
        del(cls.calc)

    def setUp(self):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        print('\n├───setUp: called before EACH test of this class')

    def test_sum_string(self):
        print("├────Test 1...")
        act = TestExample.calc.sum_string(1, 100500)
        self.assertEqual(act, 1100500, 'Метод sum_string работает неправильно.')

    def test_sum_string_first_negative_value(self):
        print("├────Test 2...")
        self.assertRaises(ValueError, TestExample.calc.sum_string, -1, 100500)

    def test_sum_string_second_negative_value(self):
        print("├────Test 3...")
        with self.assertRaises(ValueError):
            TestExample.calc.sum_string(1, -100500)

    def test_sum_args(self):
        print("├────Test 4...")
        act = TestExample.calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')

    def tearDown(self):
        """Вызывается после каждого теста."""
        print('├───tearDown: called after EACH test of this class, following dot: OK')


if __name__ == '__main__':
    unittest.main()
