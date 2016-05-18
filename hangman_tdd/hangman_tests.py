#  hangman_tests.py


import unittest
from hangman_tdd import Hangman

class Boom(Exception):
    pass

def foo(n):
    if n == 7:
        raise Boom("!")

SECRET_WORD = 'helloool'
class TestHangman(unittest.TestCase):
    def setUp(self):
        """Runs Before Each Test"""
        self.game = Hangman(SECRET_WORD, 10)

    def tearDown(self):
        """Runs Before Each Test"""
        pass

    def test_status(self):
        self.assertEquals(self.game.status(), ('?'*len(SECRET_WORD)))

    def test_good_guess(self):
        self.game.guess('h')
        self.assertEquals(self.game.status(), 'h???????')

    def test_bad_guess(self):
        self.game.guess('r')
        self.assertEquals(self.game.status(), '????????')

    def test_multiple_guess(self):
        self.game.guess('l')
        self.assertEquals(self.game.status(), '??ll???l')

    def test_multiple_guess2(self):
        self.game.guess('o')
        self.assertEquals(self.game.status(), '????ooo?')

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
