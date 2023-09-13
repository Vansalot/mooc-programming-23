def list_of_stars(list):
    for number in list:
        print('*' * number)


if __name__ == "__main__":
    list1 = [3, 7, 1, 1, 2]
    list2 = [1, 2, 3, 4, 5]
    list3 = [2, 4, 6, 4, 6, 4, 2]

    list_of_stars(list1)
    list_of_stars(list2)
    list_of_stars(list3)