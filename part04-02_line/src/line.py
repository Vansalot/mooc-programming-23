def line(times, string):
    message = string
    
    if string == '':
        message = '*'
    print(message[0] * times)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")