#
# def divide(a,b):
#     return a/b
#
#
# print(divide(5,2))
#
# print(divide(2,0))

import unittest
import arithmetic


class TestArithmetic(unittest.TestCase):

    def test_square(self):
        num = 5
        result = num/0
        self.assertNotEqual(result,0)


if __name__ == '__main__':
    unittest.main()
