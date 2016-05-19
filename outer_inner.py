def outer():

    def inner():
        print("inner", x)

    print("outer")
    x = 10
    inner()

outer()