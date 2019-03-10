def printStars(s):
    for i in range(len(s) + 3):
        print(chr(0x2605), end="")
    print("")

if __name__ == "__main__":
    s = "我喜欢数据科学导论"
    printStars(s)
    print(chr(0x2605), s, chr(0x2605))
    printStars(s)
