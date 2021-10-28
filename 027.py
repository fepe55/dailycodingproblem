"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def solve(test_string):
    # Keeps track of the last type of bracket that was opened
    order_opened = []

    for char in test_string:
        if char == '(':
            order_opened.append(char)
        elif char == '{':
            order_opened.append(char)
        elif char == '[':
            order_opened.append(char)
        elif char == ')':
            try:
                if order_opened.pop() != '(':
                    return False
            except IndexError:
                return False
        elif char == '}':
            try:
                if order_opened.pop() != '{':
                    return False
            except IndexError:
                return False

        elif char == ']':
            try:
                if order_opened.pop() != '[':
                    return False
            except IndexError:
                return False

    return len(order_opened) == 0


def solve_two(test_string):
    round = 0
    curly = 0
    square = 0
    # Keeps track of the last type of bracket that was opened
    order_opened = []

    for char in test_string:
        if char == '(':
            round += 1
            order_opened.append(char)
        elif char == '{':
            curly += 1
            order_opened.append(char)
        elif char == '[':
            square += 1
            order_opened.append(char)
        elif char == ')':
            round -= 1
            if round < 0:
                return False
            if order_opened.pop() != '(':
                return False
        elif char == '}':
            curly -= 1
            if curly < 0:
                return False
            if order_opened.pop() != '{':
                return False
        elif char == ']':
            square -= 1
            if square < 0:
                return False
            if order_opened.pop() != '[':
                return False

    return round == 0 and curly == 0 and square == 0


if __name__ == '__main__':
    test_string = "([])[]({})"
    balanced = solve(test_string)
    assert balanced
    balanced = solve_two(test_string)
    assert balanced

    test_string = "))()"
    balanced = solve(test_string)
    assert not balanced
    balanced = solve_two(test_string)
    assert not balanced

    test_string = "()()"
    balanced = solve(test_string)
    assert balanced
    balanced = solve_two(test_string)
    assert balanced

    test_string = "([)]"
    balanced = solve(test_string)
    assert not balanced
    balanced = solve_two(test_string)
    assert not balanced

    test_string = "((()"
    balanced = solve(test_string)
    assert not balanced
    balanced = solve_two(test_string)
    assert not balanced

    test_string = ""
    balanced = solve(test_string)
    assert balanced
    balanced = solve_two(test_string)
    assert balanced
