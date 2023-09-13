def line(times, string):
    message = string
    
    if string == '':
        message = '*'
    print(message[0] * times)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    index = size

    while index > 0:     
        line(size, "#")
        index -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(2)
