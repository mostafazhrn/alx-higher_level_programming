#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_lst = []
    x = 0
    while x < list_length:
        try:
            nat = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            nat = 0
        except TypeError:
            print("wrong type")
            nat = 0
        except IndexError:
            print("out of range")
            nat = 0
        finally:
            my_lst.append(nat)
        x += 1
    return my_lst
