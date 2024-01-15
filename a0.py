# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nicholas Hoang
# nchoang1@uci.edu
# 24588398

def horizontal():
    print('+-+')


def horizontal_two():
    print('+-+-+')


def vertical():
    print('| |')


def block(num):
    x = 0
    while num >= 0:
        if num == number:
            horizontal()
            vertical()
        elif num == 0:
            print(x * '  ', end='')
            horizontal()
        elif num == number - 1:
            horizontal_two()
            x += 1
            print(x * '  ', end='')
            vertical()
        else:
            print(x * '  ', end='')
            horizontal_two()
            x += 1
            print(x * '  ', end='')
            vertical()
        num -= 1

number = int(input())
block(number)