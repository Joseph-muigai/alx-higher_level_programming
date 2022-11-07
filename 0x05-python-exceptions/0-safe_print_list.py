#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        for i in my_list[:x]:
            print("{}".format(i), end ="")
            y+=1
        print()
        return y
    except Exeception:
        print()
