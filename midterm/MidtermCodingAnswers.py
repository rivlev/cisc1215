# 36 

import re
def count_letters_and_digits(s):
    count = 0
    patt = r"[a-zA-Z0-9]"
    for c in s:
        if re.match(patt, c):
            count += 1
    return count

def count_letters_and_digits2(s):
    patt = r"[a-zA-Z0-9]"
    return len(re.findall(patt, s))

def count_letters_and_digits3(s):
    count = 0
    for c in s:
        if c.isalnum():
            count += 1
    return count

def count_letters_and_digits4(s):
    return len([c for c in s if c.isalnum()])



print(count_letters_and_digits("2900 Bedford Avenue! *&^(*%)"))
print(count_letters_and_digits2("2900 Bedford Avenue! *&^(*%)"))
print(count_letters_and_digits3("2900 Bedford Avenue! *&^(*%)"))
print(count_letters_and_digits4("2900 Bedford Avenue! *&^(*%)"))

# function signature        1 point
# count logic               3 points
# match logic               3 points
# overall syntax            2 points
# return value              1 points
#                         -------------
#                           10 points


(37)
def guessing_game():
    secret = 42
    while True:
        guess = int(input("Enter your guess: "))
        if guess == secret:
            print("You guessed it!")
            return
        if guess < secret:
            print("Too low")
        else:
            print("Too high")

# function signature                        1 point
# while True / end loop appropriately       2 points
# input                                     2 points
# cast input to int                         1/2 point
# if branching logic                        2.5 points
# overall syntax                            2
#                                       ------------------
# Total                                     10 points


def every_other(fn):
    writef = open(fn[:-4] + "_every_other.txt", 'w')
    i = 0
    for line in open(fn):
        if i % 2 == 0:
            writef.write(line)
        i += 1

def every_other2(fn):
    writef = open(fn[:-4] + "_every_other.txt", 'w')
    lines = open(fn)
    for line in lines[::2]:
        writef.write(line)

# correctly create outfilename              2 points
# every other logic                         2 points
# open and read infile                      2 points
# open and write to outfile                 2 points
# syntax                                    2 points
#                                       ------------------
# Total                                     10 points


# Extra credit
x == round(x)
x % 1 == 0
x == floor(x)
x == int(x)