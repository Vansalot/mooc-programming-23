def create_tuple(x: int, y: int, z: int):
    largest = max([x, y, z])
    smallest = min([x, y, z])
    sumarium = sum([x, y, z])

    return (smallest, largest, sumarium)

if __name__=='__main__':
    print(create_tuple(5, 3, -1))