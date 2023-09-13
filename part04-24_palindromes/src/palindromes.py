# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(string):
    for index in range(0, len(string) // 2):
        if string[index] != string[len(string) - index - 1]:
            return False
    return True

def main():
    while True:
        string = input("Please type in a palindrome: ")
        if palindromes(string):
            print(f"{string} is a palindrome!")
            break
        print("that wasn't a palindrome")

main()