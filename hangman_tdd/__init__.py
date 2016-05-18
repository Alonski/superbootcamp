#  hangman.py

class Hangman:
    def __init__(self, secret_word, tries):
        self.my_guess = '?' * len(secret_word)
        self.secret_word = secret_word
        self.tries = tries

    def status(self):
        return self.my_guess

    def guess(self, letter):
        secret_set = list(self.secret_word)
        guess_set = list(self.my_guess)
        letter_count = secret_set.count(letter)
        while guess_set.count(letter) < letter_count >= 0:
            guess_set[secret_set.index(letter)] = letter
            self.my_guess = ''.join(guess_set)
            secret_set[secret_set.index(letter)] = '?'
        return letter_count


        # if self.secret_word.find(letter) >= 0:
        #     self.my_guess[self.secret_word.find(letter)] = letter
        # return self.status()


# game = Hangman("hellooo", 10)
# print(game.status())
# print(game.guess('o'))
# print(game.status())
