def line(times, string):
    message = string
    
    if string == '':
        message = '*'
    print(message[0] * times)

def triangle(size):
    # You should call function line here with proper parameters
    index = 0
    while index < size:     
        index += 1
        line(index, '#')
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)