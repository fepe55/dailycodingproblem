"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def solve(array):
    product = 1
    new_array = []
    for element in array:
        product *= element

    for element in array:
        new_array.append(int(product / element))
    return new_array


def solve_without_division(array):
    new_array = []
    for i in range(len(array)):
        array_without_me = array[:i] + array[i+1:]
        product = 1
        for elem in array_without_me:
            product *= elem
        new_array.append(product)

    return new_array


if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5]
    output = solve(input_list)
    print(output)
    output = solve_without_division(input_list)
    print(output)

    input_list = [3, 2, 1]
    output = solve(input_list)
    print(output)
    output = solve_without_division(input_list)
    print(output)
