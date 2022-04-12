"""
File: BeeperRow.py
Name: Toby
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    put_beeper()
    for i in range(9999):
        while front_is_clear():
            move()
            put_beeper()
        turn_left()
        turn_left()
        while front_is_clear():
            put_beeper()
            move()
        put_beeper()














####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)