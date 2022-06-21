#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    val = 0
    for i in mylist[:x]:
        try:
            print("{:d}".format(i), end = "")
            val += 1
        except(ValueError, TypeError):
            continue
    print("")
    return (val)
