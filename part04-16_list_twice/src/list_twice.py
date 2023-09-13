numberlist = []

while True:
    number = int(input("New item: "))
    if number == 0:
        break

    numberlist.append(number)
    print(f"The list now: {numberlist}")
    print(f"The list in order: {sorted(numberlist)}")

print("Bye!")