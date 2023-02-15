import unittest

from models import Rectangle


class TestsRectangleClass(unittest.TestCase):

    def test_id(self):
        """Test max integer function."""
        test = Rectangle(1, 2, id=-1)
        self.assertEqual(test.id, -1)
        test = Rectangle(12, 10)
        self.assertEqual(test.id, 3)
        test = Rectangle(40, 128)
        self.assertEqual(test.id, 4)
        test = Rectangle(40, 128)

    def test_widht_and_heihgt(self):
        test = Rectangle(40, 128)
        self.assertEqual(test.width, 40)
        self.assertEqual(test.height, 128)

    def test_x_and_y(self):
        test = Rectangle(1, 1)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, 0)


if __name__ == '__main__':
    unittest.main()
