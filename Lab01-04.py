def getRoot(power, exp = 2, mis = 0.00000000001):
    #Newton's method
    root = power / 2
    while abs(root ** exp - power) > mis:
        f0 = ((exp - 1) * root) / exp
        f1 = power / (exp * root ** (exp-1))
        root = f0 + f1
    return root
        
if __name__ == "__main__":
    n = eval(input("Please input a number:"))
    r = getRoot(n, 3)
    print("Its cube root is %s" % r)
