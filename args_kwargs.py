def call_twice(f, *args, **kwargs):
    return f(*args, **kwargs)

def say_hi():
    return 'hi'

def shout(s):
    print(s.upper(), "1")
    return s.upper()

print(call_twice(shout, "alon"))


