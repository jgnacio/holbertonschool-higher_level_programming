import unittest

from models import Base


class Tests(unittest.TestCase):

    def test_id(self):
        """Test max integer function."""
        test = Base()
        self.assertEqual(test.id, 1)
        test = Base(12)
        self.assertEqual(test.id, 12)
        test = Base()
        self.assertEqual(test.id, 2)
        test = Base(-44)
        self.assertEqual(test.id, -44)

    def test_to_json_string(self):
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        self.assertAlmostEqual(Base.to_json_string([]), "[]")
        test = Base.to_json_string([{"id": 1}])
        self.assertAlmostEqual(test, '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertAlmostEqual(Base.from_json_string(None), [])
        self.assertAlmostEqual(Base.from_json_string("[]"), [])
        test = Base.from_json_string('[{ "id": 89 }]')
        self.assertAlmostEqual(test, [{"id": 89}])


if __name__ == '__main__':
    unittest.main()
