def remove_smallest(numbers: list):
    sorted_number_list = sorted(numbers)
    smallest_number = sorted_number_list[0]
    numbers.remove(smallest_number)

    


if __name__=='__main__':
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)