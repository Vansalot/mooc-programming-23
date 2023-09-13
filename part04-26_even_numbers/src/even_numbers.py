def even_numbers(numberlist: list):
    evenlist = []
    for number in numberlist:
        if number % 2 == 0:    
            evenlist.append(number)
    
    return evenlist


if __name__=='__main__':
    my_list = list(range(0, 100))
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)