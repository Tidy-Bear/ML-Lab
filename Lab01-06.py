def bubbleSort(ls, order = 0):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - i - 1):
            if order == 0 and ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
            elif order == 1 and ls[j] < ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls
        
if __name__ == "__main__":
    #ls = list(eval(input("Please input several numbers separated with a comma:")))
    ls = []
    w = eval(input("Please input w:"))
    x = eval(input("Please input x:"))
    y = eval(input("Please input y:"))
    z = eval(input("Please input z:"))
    ls.append(w)
    ls.append(x)
    ls.append(y)
    ls.append(z)
    print(bubbleSort(ls, 1))
