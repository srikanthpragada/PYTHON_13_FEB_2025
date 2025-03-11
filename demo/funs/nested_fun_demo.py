g = 100 # Global variable

def f1():
    global g
    g = 200
    a = 1    # Enclosing variable
    # local function or nested function
    def f2():
        b = 2  # Local variable
        nonlocal a
        a = 10
        print(g, a, b)

    f2()
    print(a)

f1()


