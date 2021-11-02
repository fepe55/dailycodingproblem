"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single
count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
"""


def encode(string):
    length = len(string)
    i = 0
    output_string = ''
    while i < length:
        char = string[i]
        c = char
        count = 0
        while c == char and i < length:
            count += 1
            i += 1
            if i < length:
                c = string[i]
            else:
                c = ''
        output_string += f'{count}{char}'

    return output_string


def decode(string):
    output_string = ''
    length = len(string)
    i = 0
    while i < length:
        is_int = True
        string_amount = ''
        while is_int:
            try:
                int(string[i])
            except ValueError:
                is_int = False
            else:
                string_amount += string[i]
                i += 1

        amount = int(string_amount)
        letter = string[i]
        i += 1
        output_string += letter * int(amount)
    return output_string


if __name__ == '__main__':
    string = 'AAAABBBCCDAA'
    encoded_string = encode(string)
    assert encoded_string == '4A3B2C1D2A'

    decoded_string = decode(encoded_string)
    assert decoded_string == string

    string = ''
    assert decode(encode(string)) == string

    string = 'AAAAAAAAAABBBCCDAA'
    assert decode(encode(string)) == string

    string = 'AAAAAAAABBBBBBBBBBCCDDDDDDDDDDAA'
    assert decode(encode(string)) == string
