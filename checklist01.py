from __future__ import printFunction
from colors import redd, ghreen, bluue, yeaallow

checklist = list()


def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def listAllItems():
    index = 0
    for listItem in checklist:
        print(str(yeaallow(index) + bluue(listItem)))
        index += 1 #add one item to the index

def markCompleted(index):  #index is full and finished
    checklist[index] = ghreen('✓') + checklist[index]

def userInput(prompt): #prompt some user input, man!
    userInput = input(prompt) #call the prompt
    return userInput

def select(functionCode):
    if functionCode == "C" of functionCode == "c":
        inputItem = userInput("input an item: ")
        create(inputItem)

    elif functionCode == "R" or functionCode == "r":
        itemIndex = userInput("index #: ")
        print(red(read(int(itemIndex))))

    elif functionCode == "P" or functionCode == "p":
        listAllItems()

    elif functionCode == "Q" or functionCode == "q":
        return False #invalid entry

    else:
        print("invalid entry .·´¯`(>▂<)´¯`·.")
        return True

def test(): #let's test this thing
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks (X)")

    destroy(1)
    markCompleted(0)
    print(read(0))
    listAllItems()

test()
running = True

while running:
    selection = userInput(
        "press C to add to the list, press R to read from the list and P to display the list and Q to quit: ")
    runner = select(selection)
