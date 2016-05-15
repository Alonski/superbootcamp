#  letter_counter.py
from __future__ import print_function

from collections import Counter


def letter_counter(s):
    """Returns the count of letters in s.

    (string) -> dict
    Returns a dictionary. Keys are lowercase letters, values are the number of
    times this letter appears in the sentence (as a lowercase or an uppercase
    letter).
    """
    # --- WRITE YOUR CODE HERE --- #
    mydict = {}
    #  for c in s:
    #    c = c.lower()
    #    if not c.isalpha():
    #        continue
    #    if c.lower() in mydict:
    #        mydict[c] += 0
    #    else:
    #        mydict[c] = 0
    #    mydict[c] = mydict.get(c, 0) + 1
    mydict = Counter(c for c in s.lower() if c.isalpha())
    return mydict
    # ---------------------------- #


result = letter_counter("Hello world!!! HELLO!")
print("First result:", result)
expected = {'e': 2, 'd': 1, 'h': 2, 'l': 5, 'o': 3, 'r': 1, 'w': 1}
assert result == expected


result = letter_counter("""
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also the leap
into electronic typesetting, remaining essentially unchanged. It was
popularised in the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing software like
Aldus PageMaker including versions of Lorem Ipsum.
""")
print("Second result:", result)
expected = {'a': 29, 'c': 10, 'b': 5, 'e': 59, 'd': 16, 'g': 11, 'f': 6,
            'i': 38, 'h': 14, 'k': 7, 'm': 19, 'l': 22, 'o': 25, 'n': 38,
            'p': 19, 's': 39, 'r': 24, 'u': 17, 't': 43, 'w': 6, 'v': 5,
            'y': 13, 'x': 2}
assert result == expected