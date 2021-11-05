"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and the
integer is the height. Suppose it will rain and all spots between two walls
get filled up.

Compute how many units of water remain trapped on the map in O(N) time and
O(1) space.

For example:
Given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
2 in the second, and 3 in the fourth index (we cannot hold 5 since it would
run off to the left), so we can trap 8 units of water.
"""


def trapped_water(elevation_map):
    if not elevation_map or len(elevation_map) < 3:
        return 0

    running_total = 0
    left_index = 1
    right_index = len(elevation_map) - 2
    biggest_left = elevation_map[0]
    biggest_right = elevation_map[len(elevation_map) - 1]
    # lower_biggest = biggest_left if biggest_left < biggest_right else biggest_right  # noqa: E501
    lower_biggest = min([biggest_left, biggest_right])

    while left_index <= right_index:
        if elevation_map[left_index] > biggest_left:
            biggest_left = elevation_map[left_index]
            lower_biggest = min([biggest_left, biggest_right])
        else:
            running_total += lower_biggest - elevation_map[left_index]

        if left_index != right_index:
            if elevation_map[right_index] > biggest_right:
                biggest_right = elevation_map[right_index]
                lower_biggest = min([biggest_left, biggest_right])
            else:
                running_total += lower_biggest - elevation_map[right_index]
        left_index += 1
        right_index -= 1

    return running_total


# Slightly less brute force
def slightly_less_bf_trapped_water(elevation_map):
    if not elevation_map:
        return 0
    running_total = 0
    biggest_left = elevation_map[0]
    for i in range(1, len(elevation_map) - 1):
        current_elevation = elevation_map[i]
        if current_elevation > biggest_left:
            biggest_left = current_elevation
        biggest_right = max(elevation_map[i+1:])
        smaller_biggest = min([biggest_left, biggest_right])
        if smaller_biggest > current_elevation:
            running_total += smaller_biggest - current_elevation
    return running_total


# Brute force
def bf_trapped_water(elevation_map):
    running_total = 0
    for i in range(len(elevation_map)):
        if i == 0 or i == len(elevation_map) - 1:
            continue
        biggest_left = max(elevation_map[:i])
        biggest_right = max(elevation_map[i+1:])
        smaller_biggest = min([biggest_left, biggest_right])
        current_elevation = elevation_map[i]
        if smaller_biggest > current_elevation:
            running_total += smaller_biggest - current_elevation
    return running_total


if __name__ == '__main__':
    elevation_map = [2, 1, 2]
    units = trapped_water(elevation_map)
    assert units == 1

    elevation_map = [2, 3, 2]
    units = trapped_water(elevation_map)
    assert units == 0

    elevation_map = [3, 0, 1, 3, 0, 5]
    units = trapped_water(elevation_map)
    assert units == 8

    elevation_map = [3, 0, 1, 3, 0, 5, 2, 3]
    units = trapped_water(elevation_map)
    assert units == 9
