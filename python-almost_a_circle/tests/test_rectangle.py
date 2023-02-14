import unittest

from models import rectangle

class Tests(unittest.TestCase):

    def test_base(self):
        """Test max integer function."""
        test = rectangle.Rectangle()
        self.assertEqual(test.id, 1)
        test = rectangle.Rectangle(12)
        self.assertEqual(test.id, 12)
        test = rectangle.Rectangle()
        self.assertEqual(test.id, 2)

if __name__ == '__main__':
    unittest.main()
