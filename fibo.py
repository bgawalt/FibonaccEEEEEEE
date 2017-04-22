
import math
import sqlite3

from mastodon import Mastodon


def Fibonacci(a, b):
    return a + b


def NumToEeeee(num):
    if num == 0:
        return 'e'
    elif num == 1:
        return 'E'
    suffix = 'e' if num % 2 == 0 else 'E'
    return NumToEeeee(num/2) + suffix


def RegisterApp():
    are_you_sure = raw_input("Type YES to continue registering app ")
    if are_you_sure != "YES":
        return
    Mastodon.create_app('fibonacci_autoposter', scopes=['write'],
        api_base_url="https://dolphin.town", to_file="fibo_autoposter.txt")


def main():
    RegisterApp()


if __name__ == "__main__":
    main()
