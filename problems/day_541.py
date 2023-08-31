"""
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""

import unittest

sample_str = "DAAAABBBCCDACDDD"


def encode(string):
    c = count = 0
    ret_str = ""
    while c < len(string) - 1:
        if string[c] == string[c+1]:
            count += 1
        else:
            ret_str += f"{count+1}{string[c]}"
            count = 0
        c += 1
    ret_str += f"{count + 1}{string[c]}"
    return ret_str
