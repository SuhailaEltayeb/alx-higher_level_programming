#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    create_list = []

    for i in range(list_length):
        try:
            create_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            create_list.append(0)
            print('division by 0')
            continue
        except IndexError:
            create_list.append(0)
            print('out of range')
            continue
        except TypeError:
            create_list.append(0)
            print('wrong type')
            continue
        finally:
            pass

    return create_list
