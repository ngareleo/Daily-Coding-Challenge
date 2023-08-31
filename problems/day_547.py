"""
This problem was asked by Salesforce.
Given an array of integers, find the maximum XOR of any two elements.
"""


def max_xor(arr):
    u = sorted(arr, key=lambda a: bin(a).count("0"))
    return u[-1] ^ u[-2]





