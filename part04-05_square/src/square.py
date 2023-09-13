def line(times, string):
    message = string
    
    if string == '':
        message = '*'
    print(message[0] * times)

def square(size, character):
    # You should call function line here with proper parameters
    index = size

    while index > 0:     
        line(size, character)
        index -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(14, "y")