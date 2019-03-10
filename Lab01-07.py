def wordCount(data, order = 1):
    te={}
    for i in data:
        te[i]=te.get(i,0) + 1
    re = sorted(te.items(), key = lambda item:item[1],reverse = order)
    return re

if __name__ == "__main__":
    with open('Shakespeare Sonnet.txt', 'r') as f:
        s = f.read()
    #scan the passage
    sentences = s.split("\n")
    words = []
    for i in sentences:
        temp = i.split(" ")
        for j in temp:
            j = j.strip(',:;?!')
            j = j.lower()
            words.append(j)
    print(wordCount(words))
