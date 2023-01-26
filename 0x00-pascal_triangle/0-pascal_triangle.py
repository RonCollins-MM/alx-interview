#!/usr/bin/python
# -*- coding: utf-8 -*-


def pascal_triangle(n):
    """Prints the pascal triangle upto the n'th row.
    Parameters
    ----------
    n : int
        The row upto which the triangle should be printed

    Returns
    -------
    list of lists of integers
        A list of lists that represents the traingle rows and columns
    """

    # Declare empty outer list. Outer list represents the triangle.
    # row represents each row of the trianlge, which contains another list

    outer_list = []
    row = 0

    # This outer while loop ensures only n number of rows are printed

    while row < n:

        # Inner list will be populated with new numbers after
        # summation. The inner list will later be appended to outer
        # list.

        inner_list = []
        col = 0

        # This is a special case. The first row must begin with
        # a list that contains only one value: 1
        # This code is thus only run once.....

        if row == 0 and col == 0:
            inner_list.append(1)
            outer_list.append(inner_list)
            row += 1
            continue

        # This inner while loop is what populates the inner list

        while col <= row:

            # Check for the left edge of triangle. All left edge
            # values are 1

            if col - 1 == -1:
                inner_list.append(1)
                col += 1
                continue

            # Check for the right edge of traingle. All right edge
            # values are 1.
            # Once right edge is reached, go to next row.

            if col == row:
                inner_list.append(1)
                outer_list.append(inner_list)
                break

            # Code to populate values between left and
            # edges.

            first_num = outer_list[row - 1][col - 1]
            second_num = outer_list[row - 1][col]
            inner_list.append(first_num + second_num)
            col += 1
        row += 1
    return outer_list
