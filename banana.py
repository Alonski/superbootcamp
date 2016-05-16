from collections import defaultdict
from pprint import pprint

fruit = defaultdict(list)

fruit['yellow'].append('banana')
fruit['yellow'].append('pineapple')
fruit['red'].append('apple')
fruit['green'].append('pear')
fruit['green'].append('apple')

for k, v in fruit.items():
    print(k, v)


words = ["banana", "pear", "apple", "lemon", "orange", "apricot", "pineapple", "grapes", "mishmish"]

pprint(sorted(words))


def get_reversed(s):
    return s[::-1]


pprint(sorted(words, key=get_reversed))