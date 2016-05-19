#  hangman.py


class GameOver(Exception):
    def __init__(self, word):
        # Call the base class constructor with the parameters it needs
        print("Excepting", word)
        Exception.__init__(self, 'The word was "{}"'.format(word))

class Hangman:
    def __init__(self, secret_word, tries):
        self.my_guess = '?' * len(secret_word)
        self.secret_word = secret_word
        self.tries = tries

    def status(self):
        # print("Status: {}".format(self.my_guess))
        return self.my_guess

    def guess(self, letter):
        # print("Guessing {}".format(letter))
        secret_set = list(self.secret_word)
        guess_set = list(self.my_guess)
        letter_count = secret_set.count(letter)
        # print("Letter Count", letter_count)
        while guess_set.count(letter) < letter_count >= 0:
            guess_set[secret_set.index(letter)] = letter
            self.my_guess = ''.join(guess_set)
            secret_set[secret_set.index(letter)] = '?'
        if letter_count <= 0:
            self.tries -= 1
            # print("Wrong!", self.tries)
            if self.tries <= 0:
                print("Game Over!", self.secret_word)
                raise GameOver(self.secret_word)
        return letter_count

        # if self.secret_word.find(letter) >= 0:
        #     self.my_guess[self.secret_word.find(letter)] = letter
        # return self.status()

    def lets(self):
        raise GameOver(self.secret_word)

# game = Hangman("hellooo", 10)
# print(game.status())
# print(game.guess('o'))
# print(game.status())
