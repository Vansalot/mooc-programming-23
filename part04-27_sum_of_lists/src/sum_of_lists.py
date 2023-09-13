def list_sum(list1, list2):
    list_of_sums = []
    for index in range(0, len(list1)):
        list_of_sums.append(list1[index] + list2[index])
    
    return list_of_sums

def now_also_with_zip(list1, list2):
    # Just to check out the zip-function.
    list_of_sums = []
    for item1, item2 in zip(list1, list2):
        list_of_sums.append(item1 + item2)
    return list_of_sums

if __name__=='__main__':
    a = list(range(1, 100, 4))
    b = list(range(1, 100, 3))
    print(list_sum(a, b)) # [8, 10, 12]
    print(now_also_with_zip(a, b))