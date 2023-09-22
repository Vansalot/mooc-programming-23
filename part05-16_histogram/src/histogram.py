def histogram(word: str):
    histogram_dict = {}
    for letter in word:
        if letter not in histogram_dict:
            histogram_dict[letter] = 1
        elif letter in histogram_dict:
            histogram_dict[letter] += 1
    
    for letter, times in histogram_dict.items():
        print(letter, '*' * times)

if __name__ == '__main__':
    histogram("abba")
    histogram("statistically")
