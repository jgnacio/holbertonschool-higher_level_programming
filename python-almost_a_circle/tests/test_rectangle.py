import unittest

from models import Rectangle


class TestsRectangleClass(unittest.TestCase):

    def test_id(self):
        """Test max integer function."""
        r1 = Rectangle(1, 2, id=-1)
        self.assertEqual(r1.id, -1)
        r2 = Rectangle(12, 10)
        self.assertEqual(r2.id, 11)
        r3 = Rectangle(40, 128)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(40, 128)
        self.assertEqual(r4.id, 13)

    def test_widht_and_heihgt(self):
        r5 = Rectangle(40, 128)
        self.assertEqual(r5.width, 40)
        self.assertEqual(r5.height, 128)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
            Rectangle(1, "2")
            Rectangle(1, 2, "3")
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
            Rectangle(1, -2)
            Rectangle(0, 2)
            Rectangle(1, 0)
            Rectangle(1, 2, -3)
            Rectangle(1, 2, 3, -4)

    def test_x_and_y(self):
        r6 = Rectangle(1, 1)
        self.assertEqual(r6.x, 0)
        self.assertEqual(r6.y, 0)

    def test_area(self):
        r7 = Rectangle(1, 1)
        self.assertEqual(r7.area(), 1)
        r8 = Rectangle(1, 24)
        self.assertEqual(r8.area(), 24)
        r9 = Rectangle(2, 8)
        self.assertEqual(r9.area(), 16)
        self.assertEqual(r9.area(), 16.0)

    def test__str__(self):
        r10 = Rectangle(1, 1)
        self.assertEqual(str(r10), '[Rectangle] (3) 0/0 - 1/1')

    def test_display(self):
        import sys
        import io

        r11 = Rectangle(2, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r11.display()
        self.assertEqual(capturedOutput.getvalue(), "##\n##\n")
        r11 = Rectangle(2, 2, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r11.display()
        self.assertEqual(capturedOutput.getvalue(), "  ##\n  ##\n")
        r11 = Rectangle(2, 2, 2, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r11.display()
        self.assertEqual(capturedOutput.getvalue(), "\n\n  ##\n  ##\n")
        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        test_dic = {'x': 24, 'y': 62, 'id': 14, 'height': 2, 'width': 2}
        self.assertEqual(Rectangle(2, 2, 24, 62).to_dictionary(), test_dic)

    def testUpdateArgs(self):
        r12 = Rectangle(1, 1, 2, 2, 24)
        self.assertEqual(str(r12), "[Rectangle] (24) 2/2 - 1/1")
        r12.update(89)
        self.assertEqual(str(r12), "[Rectangle] (89) 2/2 - 1/1")
        r12.update(89, 2)
        self.assertEqual(str(r12), "[Rectangle] (89) 2/2 - 2/1")
        r12.update(89, 2, 3)
        self.assertEqual(str(r12), "[Rectangle] (89) 2/2 - 2/3")
        r12.update(89, 2, 3, 4)
        self.assertEqual(str(r12), "[Rectangle] (89) 4/2 - 2/3")
        r12.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r12), "[Rectangle] (89) 4/5 - 2/3")
        r12.update(**{'id': 89, 'width': 1})
        self.assertEqual(str(r12), "[Rectangle] (89) 4/5 - 1/3")
        r12.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r12), "[Rectangle] (89) 4/5 - 1/2")
        r12.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r12), "[Rectangle] (89) 3/5 - 1/2")
        r12.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(str(r12), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        Rectangle.__nb_objects = 0
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.to_dictionary(), {'x': 0, 'y': 0, 'id': 89, 'height': 1, 'width': 1} )
        r1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r1.to_dictionary(), {'x': 0, 'y': 0, 'id': 89, 'height': 1, 'width': 1} )




if __name__ == '__main__':
    unittest.main()
