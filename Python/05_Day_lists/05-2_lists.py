item_list = list()

def items(user_input):
    item_list.append(user_input)
    print("Your items include: {}".format(item_list))
    item_list.reverse()
    print("Your items in reverse order: {}".format(item_list))

while True:
    user_items = input('Add Items: ')
    if user_items.lower() == 'exit':
        print("Goodbye...")
        break
    items(user_items)