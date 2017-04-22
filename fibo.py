
import math
import sqlite3
import sys

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

'''
def RegisterApp():
    """Populate ./fibo_autoposter.txt with creds identifying the autoposter."""
    are_you_sure = raw_input("Type YES to continue registering app ")
    if are_you_sure != "YES":
        return
    Mastodon.create_app('fibonacci_autoposter', scopes=['write'],
        api_base_url="https://dolphin.town", to_file="fibo_autoposter.txt")


def CreateUserCreds():
    """Populate ./fibo_usercred.txt with creds for the actual Mastodon acct."""
    client_id = raw_input("Enter client ID: ")
    client_secret = raw_input("Enter client secret: ")
    pword = raw_input("Enter password: ")
    mastodon = Mastodon(client_id=client_id, client_secret=client_secret,
        api_base_url="https://dolphin.town")
    mastodon.log_in('bgawalt@gmail.com', pword, to_file = 'fibo_usercred.txt')

THE ABOVE TWO FUNCTIONS: I couldn't get them to work.
Instead, I followed the directions at:
    https://tinysubversions.com/notes/mastodon-bot/index.html
And copied the client info into two consecutive lines into 'fibo_autoposter.txt'
Then I copied the access token all on its own into 'fibo_usercred.txt'

You can't see those in this git repo though, they're secret.
I just SCP'ed them up to gawalt.com after cloning this repo there.
'''

def PostToDolphinTown(eeeee):
    mast = Mastodon(client_id="fibo_autoposter.txt",
        access_token="fibo_usercred.txt",
        api_base_url="https://dolphin.town")
    mast.toot(eeeee)


def CreateDatabaseAndKickStartSequence(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("create table if not exists numbers (num integer)")
    cur.execute("insert into numbers values (0)")
    cur.execute("insert into numbers values (1)")
    conn.commit()
    cur.close()
    conn.close()


def GetTopTwoNumbersFromDatabase(db_name):
    # TODO: Hey maybe make this a `with` block bud
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("select num from numbers order by num desc limit 2")
    nums = [t[0] for t in cur.fetchall()]
    if len(nums) != 2:
        raise ValueError("WHY DID MORE THAN TWO NUMS COME BACK??? " + str(nums))
    cur.close()
    conn.close()
    return sorted(nums)


def AddNumberToDatabase(num, db_name):
    # TODO: Hey maybe make this a `with` block bud
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("insert into numbers values (?)", (num,))
    cur.close()
    conn.commit()
    conn.close()


def PostNextFibo(db_name):
    a, b = GetTopTwoNumbersFromDatabase(db_name)
    c = Fibonacci(a, b)
    text = NumToEeeee(c)
    PostToDolphinTown(text)
    AddNumberToDatabase(c, db_name)


def PrintNextFibo(db_name):
    a, b = GetTopTwoNumbersFromDatabase(db_name)
    c = Fibonacci(a, b)
    text = NumToEeeee(c)
    AddNumberToDatabase(c, db_name)
    print c, text


def main(args):
    if "new_db" in args:
        CreateDatabaseAndKickStartSequence(args[1])
    PostNextFibo(args[1])


if __name__ == "__main__":
    main(sys.argv)
