def numSum(num):
    sum = 0
    for i in num:
        sum += i
    return sum

if __name__ == "__main__":
    print("The sum is %s" % numSum(range(1,101)))
