"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream
of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two
middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:

2
1.5
2
3.5
2
2
2
"""


def get_running_median(sequence):
    running_median = []
    for i in range(1, len(sequence) + 1):
        current_list = sorted(sequence[:i])
        if i % 2:  # if odd
            mid_point = i // 2
            median = current_list[mid_point]
        else:
            lower_mid_point = i//2 - 1
            higher_mid_point = i//2
            median = (
                current_list[lower_mid_point] + current_list[higher_mid_point]
            ) / 2
        running_median.append(median)

    return running_median


if __name__ == '__main__':
    sequence = [2, 1, 5, 7, 2, 0, 5]
    running_median = get_running_median(sequence)
    assert running_median == [2, 1.5, 2, 3.5, 2, 2, 2]

    sequence = []
    running_median = get_running_median(sequence)
    assert running_median == []

    sequence = [2]
    running_median = get_running_median(sequence)
    assert running_median == [2]
