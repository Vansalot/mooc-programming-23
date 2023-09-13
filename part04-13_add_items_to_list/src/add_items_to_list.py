item_list = []
item_number = int(input("How many items: "))

while len(item_list) < item_number:
    item_list.append(int(input(f"item {len(item_list) + 1}: ")))
    
print(item_list)