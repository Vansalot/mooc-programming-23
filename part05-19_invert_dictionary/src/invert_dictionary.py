def invert(dictionary: dict):
    inverted_dict = {}

    for key, item in dictionary.items():
        inverted_dict[item] = key
    dictionary.clear()
    for key, item in inverted_dict.items():
        dictionary[key] = item


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    print(s)
    invert(s)
    print(s)