checklist = list()

def create(item):
    checklist = list()
    checklist.append('Blue')
    print(checklist)
    checklist.append('Orange')
    print(checklist)


def read(index):
    item = checklist[index]
    return item
    
def update(index, item):
    checlist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")
        #item_index must exist.
        read(item_index)
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False

    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input
    user_value = user_input("Please Enter a value: ")
    print(user_value)

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    list_all_items()

    select("C")
    list_all_items()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list")
    select(selection)

test()
