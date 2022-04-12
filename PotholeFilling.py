"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
        for i in range(3):
            go_in()
            put_99()
            go_out()


def go_in():
    """
    pre_condition:Karel is out of the pothole, facing east

    post_condition:Karel is in the pothole, facing south
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre_condition:Karel is in the pothole, facing south

    post_condition:Karel is out of the pothole, facing east
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99():
    for i in range(99):
        put_beeper()







####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
