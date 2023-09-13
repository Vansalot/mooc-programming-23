def longest_series_of_neighbours(list):
    result = 1
    neigbour_count = 1
    
    for index in range(1, len(list)):
        # Check difference of current and previous index using abs()
        if abs(list[index - 1] - list[index]) == 1:
            neigbour_count += 1
        else:
            neigbour_count = 1
        result = max(result, neigbour_count)
    return result

if __name__=='__main__':
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))

    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))