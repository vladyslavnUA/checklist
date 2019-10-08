checklist = list()

# CREATE
def create(item):
    checklist.append(item)
# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + " " + list_item)
        index += 1

def mark_completed(index):
    update(index, " √ " + checklist[index])

def select(function_code):
    #create an item
    try:
        if function_code == "C" or function_code == "c":
            input_item = user_input("input an item: ")
            create(input_item)
            return True

        #read item
        elif function_code == "R" or function_code == "r":
            item_index = int(user_input("index number: "))
            #print the items user created
            print(read(item_index))
            return True

        #let's print everything
        elif function_code == "P" or function_code == "p":
            list_all_items()
            return True
        
        #quit
        elif function_code == "Q" or function_code == "q":
            user_check = user_input("do you want to quit the program? (y/n) ")
            if user_check == "Y" or user_check == "y":
                exit()
            else:
                return False

        #mark completed
        elif function_code == "M" or function_code == "m":
            item_index = int(user_input("index number: "))
            mark_completed(int(item_index))
            return True

        #update item
        elif function_code == "U" or function_code == "u":
            item_index = user_input("index number: ")
            item_input = user_input("item to update: ")
            update(int(item_index), str(item_input))
            return True

    except:
        print("not a valid entry. enter a number: ")
        return True
        

def user_input(prompt):
    user_input = input(prompt)
    return user_input

#TEST
def test():
    # create("purple sox")
    # create("red cloak")
    #
    # print(read(0))
    # print(read(1))
    #
    # update(0, "purple socks")
    # destroy(1)
    #
    # print(read(0))
    # print(read(1))
    # select(selection)

    list_all_items()

    # select(selec)

    # list_all_items()
    # name = user_input("Enter name: ")
    # print(name)
    
test()

running = True
while running:
    selection = user_input("Press C to add to list, R to read from list, E to remove, P to display list, U to update, M to mark as completed (press again to unmark), and Q to quit: ")
    running = select(selection)
