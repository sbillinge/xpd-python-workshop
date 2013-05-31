#!/usr/bin/env python

# Adjust your Python configuration in such way that it can
# be imported by "import xpdsayhello" by python process started
# in any directory.
#
# The "pydoc xpdsayhello" command should also work from any
# directory and print a description of this module and of
# the defined functions.


"""This module defines a sayhello function that prints
a greeting to the specified name or to a stranger if no
name was given.

DEFAULT_NAME -- the default person to greet when name was not specified.
"""

DEFAULT_NAME = "stranger"


def sayhello(name=None):
    '''FIXME
    '''
    if name is None:
        subject = DEFAULT_NAME
    else:
        subject = name
    print "Hello", subject + "!"
