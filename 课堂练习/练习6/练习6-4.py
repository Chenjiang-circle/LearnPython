txt = open("test.txt", "r", encoding="utf-8").read()


def filterTxt(txt):
    for ch in '!@#$%^&*()[]{};"_,.?/:|\\+-<>~`':
        txt = txt.replace(ch, "")
    return txt


txt = open("test.txt", "r", encoding="utf-8").read()
txt = filterTxt(txt)
counts = {}
for char in txt:
    if char == ' ':
        continue
    counts[char] = counts.get(char, 0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(len(items)):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
