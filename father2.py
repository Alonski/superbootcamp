#  father.py
name = "joe"
sons = 2
daughters = 3

# ----- ENTER YOUR CODE HERE --------
name = input("What is the name of the father?")
sons = int(input("How many sons does he have?"))
daughters = int(input("How many daughters"))
s = "{} has {} kids.".format(name.capitalize(), sons + daughters)
# -----------------------------------

print(s)
assert s == "Joe has 5 kids."
print("OK")
