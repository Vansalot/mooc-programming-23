def sum_of_positives(list):
    result = 0
    for number in list:
        if number > 0:
            result += number
    return result



if __name__=='__main__':
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)