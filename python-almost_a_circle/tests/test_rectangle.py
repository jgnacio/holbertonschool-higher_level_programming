#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 9:14:00 2023.

@author: jgnacio
@description:

"""

import unittest
import sys
import os
import io
from models import Rectangle, Base


class TestsRectangleClass(unittest.TestCase):
    """Test class rectangle."""

    def test_id(self):
        """Test max integer function."""
        r1 = Rectangle(1, 2, id=-1)
        self.assertEqual(r1.id, -1)
        r2 = Rectangle(12, 10)
        self.assertEqual(r2.id, 15)
        r3 = Rectangle(40, 128)
        self.assertEqual(r3.id, 16)
        r4 = Rectangle(40, 128)
        self.assertEqual(r4.id, 17)

    def test_widht_and_heihgt(self):
        """Test width and height."""
        r5 = Rectangle(40, 128)
        self.assertEqual(r5.width, 40)
        self.assertEqual(r5.height, 128)

    def test_width_height_exceptions(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, -4)

    def test_x_and_y(self):
        """Test x and y coordinates."""
        r6 = Rectangle(1, 1)
        self.assertEqual(r6.x, 0)
        self.assertEqual(r6.y, 0)

    def test_area(self):
        """Test area."""
        r7 = Rectangle(1, 1)
        self.assertEqual(r7.area(), 1)
        r8 = Rectangle(1, 24)
        self.assertEqual(r8.area(), 24)
        r9 = Rectangle(2, 8)
        self.assertEqual(r9.area(), 16)
        self.assertEqual(r9.area(), 16.0)

    def test__str__(self):
        """Test string."""
        r10 = Rectangle(1, 1)
        self.assertEqual(str(r10), '[Rectangle] (3) 0/0 - 1/1')

    def test_display(self):
        """Test display."""
        r11 = Rectangle(2, 2)
        output = io.StringIO()
        sys.stdout = output
        r11.display()
        self.assertEqual(output.getvalue(), "##\n##\n")
        r11 = Rectangle(2, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        r11.display()
        self.assertEqual(output.getvalue(), "  ##\n  ##\n")
        r11 = Rectangle(2, 2, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        r11.display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")
        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        """Test to dictionary."""
        test_dic = {'x': 24, 'y': 62, 'id': 20, 'height': 2, 'width': 2}
        self.assertEqual(Rectangle(2, 2, 24, 62).to_dictionary(), test_dic)

    def test_update_args(self):
        """Test for update arguments."""
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
        r12.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r12), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        """Test for creating a rectangle."""
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.to_dictionary(), {
            'x': 0, 'y': 0, 'id': 89, 'height': 1, 'width': 1
        })
        r1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r1.to_dictionary(), {
            'x': 0, 'y': 0, 'id': 89, 'height': 1, 'width': 1
        })
        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.to_dictionary(), {
            'x': 0, 'y': 0, 'id': 89, 'height': 2, 'width': 1
        })
        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.to_dictionary(), {
            'x': 3, 'y': 0, 'id': 89, 'height': 2, 'width': 1
        })
        r1 = Rectangle.create(**{
            'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        })
        self.assertEqual(r1.to_dictionary(), {
            'x': 3, 'y': 4, 'id': 89, 'height': 2, 'width': 1
        })

    def test_save_to_file(self):
        """test save_to_file."""
        r1 = Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        os.remove("./Rectangle.json")
        r1 = Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])
        os.remove("./Rectangle.json")
        r1 = Rectangle.save_to_file([Rectangle(1, 2, 1, 1, 20)])
        self.assertIsInstance(Rectangle.load_from_file()[0], Rectangle)
        r1 = Rectangle.load_from_file()
        self.assertEqual(Base.save_to_file(r1), None)


if __name__ == '__main__':
    unittest.main()
