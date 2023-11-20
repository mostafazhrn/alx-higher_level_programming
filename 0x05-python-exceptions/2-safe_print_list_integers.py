#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    compte = 0
    y = 0
    while y < x:
        try:
            print("{:d}".format(my_list[y]), end="")
            compte += 1
        except TypeError:
            None
        except ValueError:
            None
        y += 1
    print("")
    return compte
