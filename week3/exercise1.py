# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """

    number_list = []
    while start < stop:
        number_list.append(start)
        start += step
    return number_list


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    number_list = []
    while start < stop:
        number_list.append(start)
        start += step
    return number_list

def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    number_list = []
    while start < stop:
        number_list.append(start)
        start += 2 
   
    return number_list
    


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    
    print("Welcome this guessing game")
    lower_bound = int(low)
    higher_bound = int(high)
    bounded = False

    while not bounded:
        guess = int(input("The number: "))
        if guess< lower_bound:
            print("Guess higher try again")
        elif guess > higher_bound:
            print("Guess lower try again")
        else:
            bounded = True
            print("You got it")
    return guess              


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            value = int(input(message))
            return value
        except:
            print("Not the number, try again")



def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    
    print("Welcome the guessing game")
    lower_bounded = int(low)
    higher_bounded = int(high)
    bounded = False

    while not bounded:
        guess = str(input("Guess A number: "))
        if guess.isdigit():
            if int(guess) < lower_bounded:
                print("Guess higher")
            elif int(guess) > higher_bounded:
                 print("Guess lower")
            else:
                 bounded = True
                 print("Well done") 
        else:
            print("Please try again")
    return guess

if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
