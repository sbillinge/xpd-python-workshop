#!/usr/bin/env python
# INSTRUCTIONS:
#
# Uncomment the marked lines below and perhaps add a few more
# meaningful checks.  Run this file as
#
#   python teststringchecks.py
#
# and change the test file stringchecks.py until all tests pass.

"""Unit tests for the stringchecks.py file
"""

import unittest
from py04exceptunit.stringchecks import isint, isfloat, isStringTrue

# ----------------------------------------------------------------------------
class Test_isStringTrue(unittest.TestCase):

    def test_yesno(self):
        "check isStringTrue() for valid arguments."
        self.assertTrue(isStringTrue("yes"))
        self.assertFalse(isStringTrue("no"))
        ## +++uncomment the line below+++
        # self.assertFalse(isStringTrue("NO"))
        # self.assertFalse(isStringTrue("No"))
        return

    def test_other(self):
        """check isStringTrue() for a bad argument."""
        self.assertRaises(ValueError, isStringTrue, "dog")
        return

# ----------------------------------------------------------------------------
class Test_isint(unittest.TestCase):

    def test_stringargs(self):
        "check isint for valid argument."
        self.assertTrue(isint("1"))
        self.assertTrue(isint("-99"))
        self.assertTrue(isint(" 123  "))
        self.assertFalse(isint("1.5"))
        self.assertFalse(isint("x"))
        return

    def test_badargs(self):
        """check isint raises an exception when argument is not a string.
        """
        self.assertRaises(TypeError, isint, [])
        self.assertRaises(TypeError, isint, {})
        self.assertRaises(TypeError, isint, None)
        return

# ----------------------------------------------------------------------------
class Test_isfloat(unittest.TestCase):

    def test_stringargs(self):
        "check isfloat for valid argument."
        self.assertTrue(isfloat("1"))
        self.assertTrue(isfloat("-99"))
        self.assertTrue(isfloat(" 123  "))
        self.assertTrue(isfloat("1.5"))
        self.assertTrue(isfloat("0.0003e+8"))
        self.assertFalse(isfloat("x"))
        return


if __name__ == '__main__':
    unittest.main()
