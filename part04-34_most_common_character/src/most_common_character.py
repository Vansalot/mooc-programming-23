def most_common_character(string):
    result = ''

    for character in string:
        if result == '' or string.count(character) > string.count(result):
            result = character

    return result

if __name__=='__main__':
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))