import json

data = {
    "hi",
    23232,
    {"a": (1231, 34234)}
}

with open("data.json", "wb") as f:
    json.dump(data, f, indent=4)
