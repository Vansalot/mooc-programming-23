def all_the_longest(list):
    longest_string = []

    for string in list:
        if len(longest_string) == 0 or len(string) > len(longest_string[0]):
            longest_string = [string]
        elif len(string) == len(longest_string[0]):
            longest_string.append(string)

    return longest_string

if __name__ == '__main__':
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']