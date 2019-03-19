def function1():
    name = "steve jobs"
    print(name.upper())
    print(name.lower())
    print(name.title())

    # iterate over a string and get one char at a time
    # for ch in name:
    #     print(ch)

    print("character at 4th index: {} ".format(name[4]))

# function1()

def function2():
    # string
    # name = "steve"
    name = "madam"

    # convert string to list
    # ['s','t','e','v','e']
    listName = list(name)

    # reverse the list
    # ['e','v','e','t','s']
    listName.reverse()

    # convert the list into string
    reversedName = ''.join(listName)

    if name == reversedName:
        print('Yes.. the string is palindrome')
    else:
        print('No.. the string is NOT palindrome')



# function2()

def function3():
    name = "madam2"
    listName = list(name)
    listName.reverse()
    if name == ''.join(listName):
        print("Yes")
    else:
        print("No")

# function3()

def function4():
    """
    insert a new character in existing string
    """
    name = "madam"
    name2 = list(name)
    name2.insert(1, 'x')
    print('final: {}'.format(''.join(name2)))

# function4()

