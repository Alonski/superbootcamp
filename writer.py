import pickle
from point import Point

data = [
    "hi",
    23232,
    {"a": (1231, 34234)},
    Point(5, 7)
]

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)
