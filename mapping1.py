data = ["Israel", "Canada", "Egypt"]

expected = ["IS", "CA", "EG"]

result = [x[:2].upper() for x in data]

assert result == expected

expected = ["Israel", "Egypt"]
result = [x for x in data if x in "AEIOU"]
print(result)
print("OK")