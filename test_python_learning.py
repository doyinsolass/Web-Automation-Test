import unittest

from python_learning import add_numbers, greet, is_even


class PythonLearningTests(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Ayo"), "Hello, Ayo!")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(7, 5), 12)

    def test_is_even_true(self):
        self.assertTrue(is_even(10))

    def test_is_even_false(self):
        self.assertFalse(is_even(9))


if __name__ == "__main__":
    unittest.main()
