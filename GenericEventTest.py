import GenericEvent as GE

def summ(a, b):
    print(a+b)
    return a+b

def subtract(a, b):
    print(a-b)
    return a-b

def multiply(a, b):
    print(a*b)
    return a*b

def divide(a, b):
    print(a/b)
    return a/b

def sum_10(a, b, c, d, e, f, g, h, i, j):
    print(a+b+c+d+e+f+g+h+i+j)

if __name__ == "__main__":
    a = {'a':2, 'b':1}
    ev = GE.GenericEvent(**a)
    ev += summ
    ev += subtract
    ev += multiply
    ev += divide

    b = {'a':3, 'b':1}
    ev(**b)
    print("The variable is of type: %s" % type(a))
    print("Then variable ev is of type: %s" % type(ev))

    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # sum_10(*a)


