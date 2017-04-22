
import math
import sqlite3


def Fibonacci(a, b):
    return a + b


def NumToEeeee(num):
    if num == 0:
        return 'e'
    elif num == 1:
        return 'E'
    suffix = 'e' if num % 2 == 0 else 'E'
    return NumToEeeee(num/2) + suffix



def main():
    a, b = 0, 1
    c = Fibonacci(a, b)
    s = NumToEeeee(c)
    x = 3
    while len(s) <= 500:
        print x, '\t', c, '\t', s
        a = b
        b = c
        c = Fibonacci(a, b)
        s = NumToEeeee(c)
        x += 1


if __name__ == "__main__":
    main()
