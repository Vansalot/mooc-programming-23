def distinct_numbers(list):
    ordered_list = []
    for number in list:
        if number not in ordered_list:
            ordered_list.append(number)
    
    return sorted(ordered_list)


if __name__=='__main__':
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]