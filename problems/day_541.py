"""
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""

sample_str = "DAAAABBBCCDACDDD"


def encode(payload):
    c = count = 0
    encoded = ""
    while c < len(payload) - 1:
        if payload[c] == payload[c+1]:
            count += 1
        else:
            encoded += f"{count+1}{payload[c]}"
            count = 0
        c += 1
    encoded += f"{count + 1}{payload[c]}"
    return encoded
