def dict_of_numbers():
    the_dict = {}
    ones_dict = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six", "7":"seven","8":"eight","9":"nine"}
    tentotwenty_dict = {"10":"ten","11":"eleven","12":"twelve","13":"thirteen","14":"fourteen","15":"fifteen","16":"sixteen", "17":"seventeen","18":"eighteen","19":"nineteen"}
    tens_dict = {"2":"twenty","3":"thirty","4":"forty","5":"fifty","6":"sixty", "7":"seventy","8":"eighty","9":"ninety"}

    the_dict[0] = "zero"
    for key, item in ones_dict.items():
        the_dict[int(key)] = item

    for key, item in tentotwenty_dict.items():
        the_dict[int(key)] = item

    for ten_key, ten_item in tens_dict.items():
        # round numbers
        the_dict[int(ten_key + '0')] = ten_item
        for one_key, one_item in ones_dict.items():
            the_dict[int(ten_key + one_key)] = ten_item + '-' + one_item
    return the_dict


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
    print(numbers[20])