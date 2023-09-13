list = []

while True:
    print("The list is now", list)
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == 'x':
        break
    elif command == 'd':
        list.append(len(list) + 1)
    elif command == 'r':
        list.pop(len(list) - 1)

print("Bye!")