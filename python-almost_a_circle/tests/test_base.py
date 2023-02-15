import unittest

from models import Base


class Tests(unittest.TestCase):

    def test_base(self):
        """Test max integer function."""
        test = Base()
        self.assertEqual(test.id, 1)
        test = Base(12)
        self.assertEqual(test.id, 12)
        test = Base()
        self.assertEqual(test.id, 2)
        test = Base(44)
        self.assertEqual(test.id, 44)


if __name__ == '__main__':
    unittest.main()
