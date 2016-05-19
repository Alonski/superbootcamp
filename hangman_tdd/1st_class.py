words = ['car', 'apple', 'door', 'banana', 'pasta']


# def get_length(w):
#     return len(w), w
#
# x = get_length  # FUNCTIONS ARE 1ST CLASS CITIZENS

print(sorted(words, key=lambda w: (len(w), w)))
