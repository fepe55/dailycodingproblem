"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive)
with uniform probability, implement a function rand7() that returns an
integer from 1 to 7 (inclusive).
"""


import random

TUPLES = [(x, y) for x in range(1, 6) for y in range(1, 6)]


def rand5():
    return random.randint(1, 5)


def rand7():
    n = 5 * (rand5() - 1) + rand5()
    if n > 21:
        return rand7()
    return ((n - 1) // 3) + 1


def rand7_first_try():
    t = rand5(), rand5()
    for i in range(7):
        if t in TUPLES[3*i:3*i+3]:
            return i + 1
    return rand7()


if __name__ == '__main__':
    occurences = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
    }
    ITERATIONS = 1000000
    expected_probability = 1 / 7
    for i in range(ITERATIONS):
        n = rand7()
        occurences[n] += 1

    # for k, v in occurences.items():
    #     print(k, v)

    for k, v in occurences.items():
        actual_probability = v / ITERATIONS
        expected_probability_int = int(expected_probability * 100)
        assert int(actual_probability * 100) == (expected_probability_int)
