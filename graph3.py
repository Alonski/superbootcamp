# graph3.py

data = [
    ['January', 5],
    ['February', 20],
    ['March', 16],
    ['April', 3],
    ['May', 7],
    ['June', 7],
    ['July', 19],
    ['August', 6],
    ['September', 3],
    ['October', 8],
    ['November', 3],
    ['December', 19],
]

for month, date in data:
    print("{:>20} |{}".format(month, "=" * date))
