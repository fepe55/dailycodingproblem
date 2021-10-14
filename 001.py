"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers
from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def brute_force(lst, k):
    for idx, n in enumerate(lst):
        for m in lst[idx:]:
            if n + m == k:
                print(f'{n} + {m} = {k}')
                return True
    return False


def add_up(lst, k):
    # return brute_force(lst, k)
    if not len(lst):
        return False
    sorted_list = sorted(set(lst))
    first_idx = 0
    last_idx = len(sorted_list) - 1
    first = sorted_list[first_idx]
    last = sorted_list[last_idx]
    while first + last != k and first != last:
        if first + last < k:
            first_idx += 1
        else:
            last_idx -= 1
        first = sorted_list[first_idx]
        last = sorted_list[last_idx]

    if first + last == k:
        print(f'{first} + {last} = {k}')
        return True
    return False


if __name__ == '__main__':
    lst = [10, 15, 3, 7]
    k = 17

    print('First case')
    print(brute_force(lst, k))
    print(add_up(lst, k))

    lst = [10, 15, 3, 7]
    k = 19

    print('Second case')
    print(brute_force(lst, k))
    print(add_up(lst, k))

    lst = []
    k = 100

    print('Third case')
    print(brute_force(lst, k))
    print(add_up(lst, k))
    lst = [10, 15, 3, 7, 1, 2, 3, 4, 5, -6, 7, 8, 9, 10, 98, 100, 150]*1000
    k = 1000000000000

    print('Fourth case')
    print(brute_force(lst, k))
    print(add_up(lst, k))
