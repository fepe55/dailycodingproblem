"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.
"""


def solve(message):
    if not message:
        return 1
    if len(message) == 1:
        if message == '0':
            return 0
        return 1
    first_two = int(message[:2])
    if first_two <= 26:
        return solve(message[1:]) + solve(message[2:])
    else:
        return solve(message[1:])


# solve(2627) -> solve(627) + solve(27)
# solve(627) -> solve(27)
# solve(27) -> solve(7)
# solve(7) -> 1
#
# solve(2627) -> 2

# solve(110) -> solve(10) + solve(0)
# solve(10) -> solve(0) + solve()
# solve(0) -> 0
# solve() -> 1
#
# solve(110) -> 0


if __name__ == '__main__':
    message = '1010'
    output = solve(message)
    print(output)
    print(output == 2)  # jj

    message = '10'
    output = solve(message)
    print(output)
    print(output == 1)  # j

    message = '9999'
    output = solve(message)
    print(output)
    print(output == 1)  # iiii

    message = '2627'
    output = solve(message)
    print(output)
    print(output == 2)  # bfbg, zag

    message = '110'
    output = solve(message)
    print(output)
    print(output == 1)  # ae

    message = '111'
    output = solve(message)
    print(output)
    print(output == 3)  # aaa, ka, ak

    message = '1111'
    output = solve(message)
    print(output)
    print(output == 5)  # aaaa, aak, aka, kaa, kk
