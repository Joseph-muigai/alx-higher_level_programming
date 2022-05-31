#!/usr/bin/python3
for i in range(0,89):
    if i % 11 == 0:
        continue
    if i == 89:
        print("{}".format(i))
    else:
        print("{}".format(i), end=(", "))
