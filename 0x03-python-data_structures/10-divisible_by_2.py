#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    Towdevidents = []
    for i in my_list:
        if (i % 2) == 0:
             Towdevidents.append(True)
        else:
             Towdevidents.append(False)
    return Towdevidents
