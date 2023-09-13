itemlist = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    if index < 0 or index >= len(itemlist):
        print("Index is outside the range of the list")
        continue
    
    itemlist[index] = int(input("New Value: "))
    print(itemlist)