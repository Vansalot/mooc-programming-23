def factorials(n: int):
    factorial_dict = {}
    factorial_dict[1] = 1
    for number in range(2, n + 1):
        factorial_dict[number] = factorial_dict[number - 1] * number
    return factorial_dict

if __name__ == '__main__':
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])