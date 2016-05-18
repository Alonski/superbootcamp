import unittest

from point import Point


class PointTestCase(unittest.TestCase):
    def test_add(self):
        """test adding two point"""
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = p1 + p2
        assert p3.x == 4
        assert p3.y == 6

    def test_sub(self):
        """test subtract two points"""
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = p1 - p2
        assert p3.x == -2
        assert p3.y == -2

    # def test_divide_by_zero(self):
    #     x = 100 / 0
    #
    # def test_assert_something_wrong(self):
    #     assert 1 == 0


if __name__ == '__main__':
    unittest.main()
