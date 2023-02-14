child_list = []
per_hour = 12.5


def total_children():
    global child_list
    child_count = 0
    for child_ in child_list:
        child_count += 1
    return child_count


def print_roll():
    print(f"Total kids: {total_children()}")
    global child_list
    for child_ in child_list:
        print(child_)


while True:
    print("Welcome")
    error_ = False
    try:
        option = int(input("Check in: (1)\nCheck out: (2)\nCalculate cost: (3)"
                           "\nPrint roll: (4)\nExit: (5)\nOption: "))
    except ValueError:
        print("Invalid answer")
        error_ = False
    if option == 1:
        child_name = input("Childs name to check in: ")
        child_list.append(child_name)
    elif option == 2:
        child_name = input("Childs name to check out: ")
        if child_name in child_list:
            child_list.remove(child_name)
            print("Child removed successfully")
        else:
            print("Child wasn't found in the daycare")
    elif option == 3:
        print(f"Cost for all kids: {total_children() * per_hour}")
    elif option == 4:
        print_roll()
    elif option == 5:
        exit("Program exited")
    else:
        print("Invalid answer")
