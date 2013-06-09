#!/usr/bin/env python

# INSTRUCTIONS:
#
# (1) add parent directory to a pth file so that "import py04exceptunit" works.
#
# (2) execute in a terminal (or command prompt):
#       python -m py04exceptunit.tests.teststringchecks
#     This will perform unit tests for this file.
#
# (3) Edit the marked part of this file and repeat step (2) until all
#     tests pass
#
# HINT 1: int("1") converts string to an integer, float("3.3") converts to
# float
#
# HINT 2: In Python shell call the int and float functions with different
# string arguments and observe what happens.
# ----------------------------------------------------------------------------

"Functions that check if string is convertible to another type."


def isint(s):
    'Return True if string can be converted to an integer.'
    # +++your code here+++
    return


def isfloat(s):
    'Return True if string can be converted to a floating point value'
    # +++your code here+++
    return

def isStringTrue(s):
    '''Translate string to its logical value.

    Return True or False.
    Raise ValueError if the string is not understood.
    '''
    if s == "yes":
        return True
    elif s == "no":
        return False
    else:
        emsg = 'String must be either "yes" or "no".'
        raise ValueError(emsg)
