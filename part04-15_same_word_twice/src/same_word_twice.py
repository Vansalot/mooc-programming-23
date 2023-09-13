wordlist = []

while True:
    word = input("Word: ")
    if word in wordlist:
        break
    wordlist.append(word)
print(f"You typed in {len(wordlist)} different words")