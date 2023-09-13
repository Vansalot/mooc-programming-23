
def spruce(size):
    print("a spruce!")
    level = 1
    while level <= size:
        padding = size - level
        stars = 2 * level - 1
        print(' ' * padding + '*' * stars)
        level += 1
    print(' ' * (size - 1) + '*')



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)