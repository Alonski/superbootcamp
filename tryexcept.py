def foo():
    for i in range(10):
        try:
            x = 10 / (7-i)
            print(x)
            return x
        except ZeroDivisionError:
            print("Skip")
        except Exception as e:
            print(e)
        finally:
            x = 80
            print("Finally")
    print("Done")

foo()