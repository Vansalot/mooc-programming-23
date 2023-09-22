def add_number(phonebook):
    name = input('name: ')
    phonenumber = input('number: ')
    phonebook[name] = phonenumber
    print('ok!')

def search_number(phonebook):
    name = input('name: ')
    if name in phonebook:
        print(phonebook[name])
    else:
        print('no number')

def main():
    phonebook = {}
    while True:
        command = input('Command (1 search, 2 add, 3 quit): ')
        if command == '3':
            break
        elif command == '2':
            add_number(phonebook)
        elif command == '1':
            search_number(phonebook)
    print('quitting...')            


main()