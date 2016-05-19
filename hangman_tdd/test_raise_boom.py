import unittest


class Boom(Exception):
    pass


def foo(n):
    if n == 7:
        raise Boom("!")


class TestBoom(unittest.TestCase):
    def test_six(self):
        foo(6)

    def test_seven(self):
        with self.assertRaises(Boom):
            foo(7)

            # self.assertRaises(Boom, foo, 7)
            # try:
            #     foo(7)
            #     assert False, "Not Good!"
            # except Boom:
            #     pass


            # def test_won(self):
            #     self.game.guess_word(SECRET_WORD)
            #     self.assertEquals(self.)


if __name__ == '__main__':
    unittest.main()
