def oddCount(num):
    odd = []
    c = 0
    for i in num:
        if i % 2 != 0:
            odd.append(i)
            c += 1
    return odd

if __name__ == "__main__":
    print("Odd numbers from 1 to 100 is %s" % oddCount(range(1,101)))
