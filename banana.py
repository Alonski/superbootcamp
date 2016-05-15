from collections import defaultdict

fruit = defaultdict(list)

fruit['yellow'].append('banana')
fruit['yellow'].append('pineapple')
fruit['red'].append('apple')
fruit['green'].append('pear')
fruit['green'].append('apple')

for k, v in fruit.items():
    print(k, v)