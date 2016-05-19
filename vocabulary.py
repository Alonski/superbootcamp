# vocabulary.py
from collections import Counter


def check_words(filename, tests):
    results = Counter()
    with open(filename) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            for title, func in tests.items():
                results[title] += func(s)
    return results

tests = {
    "Words with more than 3 letters": lambda w: len(w) > 3,
    "Words that start with a vowel (a, e, i, o, u)": lambda w: w[0] in 'aeiou',
    "Words that end with a vowel (a, e, i, o, u)": lambda w: w[-1] in 'aeiou',
    "All Words": lambda w: True,
    "Words that have only vowels": lambda w: all([l in "aeiou" for l in w]),
    "Words that don't have vowels": lambda w: all([l not in "aeiou" for l in w]),
    "Word starts and ends with the same letter (but has at least two letters)": lambda w: (w[0] == w[-1] if len(w) >= 2 else 0),
    }

results = check_words('wordsEn.txt', tests)
for k, v in results.items():
    print(k, v)
