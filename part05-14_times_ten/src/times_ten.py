def times_ten(start_index: int, end_index: int):
    dict = {}
    for number in range(start_index, end_index + 1):
        dict[number] = number * 10
    return dict


if __name__=='__main__':
    d = times_ten(11, 16)
    print(d)