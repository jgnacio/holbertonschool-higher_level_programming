#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 9:14:00 2023.

@author: jgnacio
@description:

"""

import unittest
from models import Base, Rectangle, square


class TestSquareClass(unittest.TestCase):
    """Test class square."""

    def test_square(self):
        self.assertEqual(square.Square(1).width, 1)
        self.assertEqual(square.Square(1, 2).x, 2)
        self.assertEqual(square.Square(1, 2, 3).y, 3)
        self.assertEqual(square.Square(1, 2, 3, -2).id, -2)
        with self.assertRaises(TypeError):
            square.Square("1")
            square.Square("1", 1)
            square.Square(1, "1")
            square.Square(1, 2, "3")
        with self.assertRaises(ValueError):
            square.Square(-1)
            square.Square(1, -2)
            square.Square(1, 2, -3)
            square.Square(0)

    def test_string(self):
        self.assertEqual(square.Square(1, 2, 3, 4).__str__(), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        """Test to dictionary."""
        test_dic = {'id': 62, 'x': 2, 'size': 2,  'y': 24}
        self.assertEqual(square.Square(2, 2, 24, 62).to_dictionary(), test_dic)

    def test_update_args(self):
        """Test for update arguments."""
        sq12 = square.Square(1, 1, 2, 2)
        self.assertEqual(str(sq12), "[Square] (2) 1/2 - 1")
        sq12.update(89)
        self.assertEqual(str(sq12), "[Square] (89) 1/2 - 1")
        sq12.update(89, 2)
        self.assertEqual(str(sq12), "[Square] (89) 1/2 - 2")
        sq12.update(89, 2, 3)
        self.assertEqual(str(sq12), "[Square] (89) 3/2 - 2")
        sq12.update(89, 2, 3, 4)
        self.assertEqual(str(sq12), "[Square] (89) 3/4 - 2")
        sq12.update(**{'id': 89, 'width': 1})
        self.assertEqual(str(sq12), "[Square] (89) 3/4 - 1")
        sq12.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(sq12), "[Square] (89) 3/4 - 1")
        sq12.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(sq12), "[Square] (89) 3/4 - 1")
        sq12.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(sq12), "[Square] (89) 3/4 - 1")

    def test_create(self):
        """Test for creating a square."""
        r1 = square.Square.create(**{'id': 62})
        self.assertEqual(r1.to_dictionary(), {
            'id': 62, 'x': 0, 'size': 1,  'y': 0
        })
        r1 = square.Square.create(**{'id': 62, 'x': 2})
        self.assertEqual(r1.to_dictionary(), {
            'id': 62, 'x': 2, 'size': 1,  'y': 0
        })
        r1 = square.Square.create(**{'id': 62, 'x': 2, 'size': 2})
        self.assertEqual(r1.to_dictionary(), {
            'id': 62, 'x': 2, 'size': 2,  'y': 0
        })
        r1 = square.Square.create(**{'id': 62, 'x': 2, 'size': 2,  'y': 24})
        self.assertEqual(r1.to_dictionary(), {
            'id': 62, 'x': 2, 'size': 2,  'y': 24
        })
        r1 = Rectangle.create(**{
            'id': 62, 'x': 2, 'size': 2,  'y': 24
        })
        self.assertEqual(r1.to_dictionary(), {
            'id': 62, 'width': 1, 'height': 1, 'x': 2, 'y': 24
        })

    def test_save_to_file(self):
        """test save_to_file."""
        self.assertEqual(square.Square.save_to_file(None), None)
        self.assertEqual(square.Square.save_to_file([]), None)
        self.assertEqual(square.Square.save_to_file(
            [square.Square(1, 2, 1, 1)]
        ), None)
        self.assertEqual(square.Square.save_to_file(
            [square.Square(1, 2, 1, 1)]
        ), None)
        r1 = square.Square.load_from_file()
        self.assertEqual(Base.save_to_file(r1), None)


if __name__ == '__main__':
    unittest.main()
