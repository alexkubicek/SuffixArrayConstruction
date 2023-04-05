import sys


def get_suffixes(text):
    suffixes = []
    while len(text) > 0:
        suffixes.append(text)
        text = text[1:]
    return suffixes


if __name__ == '__main__':
    filePath = input()
    inFile = open(filePath)
    for line in inFile:
        input_text = line
    inFile.close()
    if input_text.endswith("\n"):
        input_text = input_text[0:len(input_text)-1]
    if not input_text.endswith('$'):
        input_text += "$"
    patterns = get_suffixes(input_text)
    suffix_dict = {}
    i = 0
    for p in patterns:
        suffix_dict[p] = i
        i += 1
    patterns.sort()
    # print(patterns)
    f = open("output.txt", 'w')
    sys.stdout = f
    for p in patterns:
        print(suffix_dict[p], end=" ")
    f.close()
