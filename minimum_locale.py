"""
Small example of recursion
"""

def find_minimum(table):
    """
    This function finds the local minimum in a list of integer T

    Assumptions:
    - T[0] > T[1] and T[n-2] < T[n-1]
    - all values are different
    """

    #base step
    if len(table) <= 3:
        return min(table)

    #recursion
    middle = (len(table)-1)//2

    if table[middle] < table[middle+1]:
        if __debug__:
            print(table[:middle+2])
        return find_minimum(table[:middle+2])
    else:
        if __debug__:
            print(table[middle:])
        return find_minimum(table[middle:])


MY_TABLE = [10, 5, 4, 8, 2, 7, 22, 1, 11, 14]

print("The minimum value is ", find_minimum(MY_TABLE))
