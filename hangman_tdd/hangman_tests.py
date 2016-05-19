#  hangman_tests.py


import unittest
from hangman_tdd import Hangman, GameOver

SECRET_WORD = 'helloool'


class GameOver(Exception):
    def __init__(self, word):
        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, 'The word was "{}"'.format(word))


class TestHangman(unittest.TestCase):
    def setUp(self):
        """Runs Before Each Test"""
        self.game = Hangman(SECRET_WORD, 10)

    def tearDown(self):
        """Runs Before Each Test"""
        pass

    def test_status(self):
        self.assertEquals(self.game.status(), ('?' * len(SECRET_WORD)))

    def test_good_guess(self):
        self.game.guess('h')
        self.assertEquals(self.game.status(), 'h???????')

    def test_bad_guess(self):
        self.game.guess('r')
        self.assertEquals(self.game.status(), '????????')

    def test_two_letters_in_word_guess(self):
        self.game.guess('l')
        self.assertEquals(self.game.status(), '??ll???l')

    def test_many_letters_in_word_guess(self):
        self.game.guess('o')
        self.assertEquals(self.game.status(), '????ooo?')

    def test_multiple_correct_guesses(self):
        self.game.guess('h')
        # print(self.game.status())
        self.game.guess('e')
        # print(self.game.status())
        self.game.guess('l')
        # print(self.game.status())
        self.game.guess('o')
        # print(self.game.status())
        self.assertEquals(self.game.status(), 'helloool')

    def test_multiple_mixed_guesses(self):
        self.game.guess('h')
        # print(self.game.status())
        self.game.guess('r')
        # print(self.game.status())
        self.game.guess('l')
        # print(self.game.status())
        self.game.guess('q')
        # print(self.game.status())
        self.assertEquals(self.game.status(), 'h?ll???l')

    def test_tries_left(self):
        self.assertEquals(self.game.tries, 10)
        self.game.guess('h')
        self.assertEquals(self.game.tries, 10)
        self.game.guess('r')
        self.assertEquals(self.game.tries, 9)
        self.game.guess('o')
        self.assertEquals(self.game.tries, 9)

    def test_game_over(self):
        def lets_raise(letter):
            self.game.lets()
            for i in range(10):
                self.game.guess(letter)

        self.assertRaises(GameOver, lets_raise, 'r')


if __name__ == '__main__':
    unittest.main()
