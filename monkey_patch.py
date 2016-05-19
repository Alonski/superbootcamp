#  monkey_patch.py

import time


def calculate_life():
    time.sleep(0.5)
    return 42

#  -----------

result = []
old = calculate_life


def calculate_life():
    if not result:
        result.append(old())
    return result[0]

#  -----------

for n in range(10):
    print(calculate_life())
