
def mapLengthList(words):
    return [len(word) for word in words]


if __name__ == "__main__":
    words = ['ab', 'cde', 'erty']
    print (mapLengthList(words))