def line(times, string):
    message = string
    
    if string == '':
        message = '*'
    print(message[0] * times)

def shape(shape_width, triangle_char, rectangle_height, rectangle_char):
    # You should call function line here with proper parameters
    index = 0
    while index < shape_width:     
        index += 1
        line(index, triangle_char)
    
    index = 0
    while index < rectangle_height:
        index += 1
        line(shape_width, rectangle_char)

       # You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")