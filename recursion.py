"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)



# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)


do_something(4)


def calculating_blocks(rows):
    if rows < 0:
        return 0
    return rows + calculating_blocks(rows - 1)


def pyramid():
    row_chosen = int(input("how many rows - "))
    print("for {} rows, you need {} blocks".format(row_chosen, calculating_blocks(row_chosen)))


pyramid()
