def everything_reversed(list):
    newlist = []
    for word in list:
        newlist.append(word[::-1])
    
    return newlist[::-1]




if __name__=='__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)