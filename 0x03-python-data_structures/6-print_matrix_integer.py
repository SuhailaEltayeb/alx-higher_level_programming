#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for printed_matrix in matrix:
        if len(printed_matrix) == 0:
            print()
        for i in range(len(printed_matrix)):
            print("{:d}".format(printed_matrix[i]),
                    end="\n" if i is len(printed_matrix) - 1 else "")
