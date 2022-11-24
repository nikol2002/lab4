import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 100), 100)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(0, 100), -100)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-10, 2), -20)
        self.assertEqual(calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-10, 2), -5)
        self.assertEqual(calc.divide(0, 100), 0)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
