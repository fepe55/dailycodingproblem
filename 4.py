import random

"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example,
the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def solve(input_array):
    min_value = 1
    input_array.sort()
    for elem in input_array:
        if elem < min_value:
            continue
        if elem > min_value:
            return min_value
        min_value += 1
    return min_value


if __name__ == '__main__':
    input_array = [3, 4, -1, 1]
    output = solve(input_array)
    print(output == 2)

    input_array = [1, 2, 0]
    output = solve(input_array)
    print(output == 3)

    input_array = [
        17, 19, 18, 20, 21, 1, 2, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        15, 16
    ]
    output = solve(input_array)
    print(output == 22)

    input_array = [
        17, 19, 18, 20, 21, 1, 2, 0, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15,
        16
    ]
    output = solve(input_array)
    print(output == 8)

    input_array = list(range(999))
    random.shuffle(input_array)
    output = solve(input_array)

    input_array = list(range(9999))
    random.shuffle(input_array)
    output = solve(input_array)

    input_array = list(range(99999))
    input_array.remove(788)
    random.shuffle(input_array)
    output = solve(input_array)
    print(output == 788)
