"""
This problem was asked by Apple.
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
from time import sleep


def func_a():
    print("Hello User")


def func_b(f, n):
    sleep(n)
    f()


if __name__ == '__main__':
    func_b(func_a, 5)
    