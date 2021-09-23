import sys


farmer = 'farmer'
fox = 'fox'
goose = 'goose'
beans = 'beans'

items = [farmer, fox, goose, beans]
banks = [items[:], []]


def check_for_win():
    items.sort()
    banks[1].sort()
    if banks[1] == items:
        result = True
    else:
        result = False
    return result


def check_for_loss():
    result = False
    for bank in banks:
        if farmer not in bank:
            if fox in bank and goose in bank:
                print("\nThe fox ate the goose.\n")
                result = True
            if goose in bank and beans in bank:
                print("\nThe goose ate the beans.\n")
                result = True
    return result


def find_farmer():
    for i, bank in enumerate(banks):
        if farmer in bank:
            b = i
    return b


def transport(item=None):

    # Whgt bank is the farmer in?
    b = find_farmer()

    # Get the farmer's index
    fidx = banks[b].index(farmer)

    # Transpor the item
    if b == 0:
        banks[1].append(banks[0].pop(fidx))
        if item in banks[0]:
            idx = banks[0].index(item)
            banks[1].append(banks[0].pop(idx))
            msg = f" and the {item}"
        else:
            msg = ''
        print(f"The farmer{msg} moved to other bank.")

    else:
        banks[0].append(banks[1].pop(fidx))
        if item in banks[1]:
            idx = banks[1].index(item)
            banks[0].append(banks[1].pop(idx))
            msg = f" and the {item}"
        else:
            msg = ""
        print()
        print(f"The farmer{msg} moved to other bank.")
        print()

    print_screen()

    if check_for_loss():
        print("\nYou lose!\n")
        sys.exit()
    if check_for_win():
        print("\nYou win!\n")
        sys.exit()


def print_screen():
    for bank in banks:
        bank.sort()
        options = []
        for i, item in enumerate(bank):
            option = f"{i}. {item}"
            options.append(option)
        print(", ".join(options))
        if bank == banks[0]:
            print("~"*50)
            print("~"*50)
            print("~"*50)


def t(item=None):
    transport(item)


def turn():
    while True:
        print()
        print("Enter the number of the item to go across with the farmer.")
        print("If you only want to transport the farmer, enter his number.")
        print("If you want to quit, enter 'Q'.")
        selection = input(">>> ")

        # Quit
        if selection[0].upper() == 'Q':
            sys.exit()

        # Where is the farmer?
        location = find_farmer()

        # Figure out the options on the bank where the farmer is
        list_length = len(banks[location])
        options = list(range(list_length))
        options = [str(option) for option in options]

        # Did we get a valid option?
        if selection in options:
            selection = int(selection)
            print(banks[location])
            selection = banks[location][selection]
            transport(selection)




header = "The Famer, the Fox, the Goose, and the Beans."

instructions = """
You are a farmer who just bought a fox, a goose,
and a sack of beans. You need to get all of them
across the river, but your boat will only carry
you plus one other.

  * If you leave the fox with the goose, he will
    eat her.
  * If you leave the goose with the beans, she
    will eat them.

How do you get them across, one at a time, without
losing anything?
"""
print()
print("*"*50)
print(header)
print("*"*50)
print()
print(instructions)
print_screen()

turn()
