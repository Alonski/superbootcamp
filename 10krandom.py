#  10krandom.py
import random
import time

go = set()
count = 0
for i in range(10000):
    go.add(random.randint(1, 1000000))

mytime = time.time()
for i in range(10000):
    if random.randint(1, 1000000) in go:
        count += 1
print(time.time() - mytime)
print(count)

print(len(go))
#  go = []
#  count = 0
#  for i in range(10000):
#      go.append(random.randint(1, 1000000))
go = list(go)
mytime = time.time()
for i in range(10000):
    if random.randint(1, 1000000) in go:
        count += 1
print(time.time() - mytime)
print(count)
print(len(go))
