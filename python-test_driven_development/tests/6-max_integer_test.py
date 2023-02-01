import unittest

class TestStringMethods(unittest.TestCase):

    def test_max_integer(self):
        """Test max integer function."""
        max_integer = __import__("6-max_integer").max_integer
        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([1^2, 200, -30, 2000/2]), 1000)
        self.assertEqual(max_integer(), None)
        with self.assertRaises(TypeError):
            max_integer(1)

if __name__ == '__main__':
    unittest.main()
