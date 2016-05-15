# graph2.py

data = [
    10,
    3,
    2,
    16,
    8,
    3,
    7,
    9,
    12,
    16,
    0,
    4,
    10,
]
biggest = max(data)
for num in data:
    c = "*" if num == biggest else "="
    print(c * num)

