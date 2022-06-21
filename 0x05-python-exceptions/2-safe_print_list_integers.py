#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        y = 0
        for i in my_list[:x]:
            if type(i) != int:
                pass
            else:
                print("{:d}".format(i))
                y += 1
        print()
        return y
    except Exception:
        pass
