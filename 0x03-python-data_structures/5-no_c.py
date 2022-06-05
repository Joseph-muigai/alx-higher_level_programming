#!/usr/bin/python3
def no_c(my_string):
    for i in string:
        if (i == 'c') or (i =='C'):
            my_string = mystring[:mystring.index(i)] \
                    + my_string[my_string.index(i) + 1:]
    return my_string
