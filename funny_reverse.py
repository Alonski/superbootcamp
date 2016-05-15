def funny(s):
    # === YOUR CODE HERE! ===
    #  s = s.split()
    #  news = [word[::-1].lower().title() for word in s.split()]
    return ' '.join([word[::-1].lower().title() for word in s.split()])
    # for word in s:
    #    word = word[::-1].lower().title()
    #    news.append(word)
    #  return ' '.join(news)
    # =======================


result = funny("Foo bar")
print(result)
assert result == "Oof Rab"

result = funny("The quick brown fox")
print(result)
assert result == "Eht Kciuq Nworb Xof"

print("OK")