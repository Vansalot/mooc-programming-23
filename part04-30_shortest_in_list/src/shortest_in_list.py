def shortest(list):
    shortest_string = ''

    for string in list:
        if shortest_string == '' or len(string) < len(shortest_string):
            shortest_string = string
    
    return shortest_string


if __name__ == '__main__':
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)