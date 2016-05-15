#  father.py
name = "joe"
sons = 2
daughters = 3

# ----- ENTER YOUR CODE HERE --------
s = "{} has {} kids.".format(name.capitalize(), sons+daughters)
# -----------------------------------

print(s)
assert s == "Joe has 5 kids."
print("OK")
