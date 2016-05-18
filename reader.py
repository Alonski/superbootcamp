import pickle

with open('data.pickle', "rb") as f:
    print(pickle.load(f))