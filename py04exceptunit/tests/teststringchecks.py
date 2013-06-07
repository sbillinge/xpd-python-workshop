#!/usr/bin/env python

"""Unit tests for the isStringTrue function.
"""

import unittest
from py04exceptunit.stringchecks import isint, isfloat

##############################################################################
class Test_isint(unittest.TestCase):

    def test_stringargs(self):
        "check isint for valid argument."
        self.assertTrue(isint("1"))
        self.assertTrue(isint("-99"))
        self.assertTrue(isint(" 123  "))
        self.assertTrue(isint("0xff"))
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

# End of class Test_isint

##############################################################################
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

# End of class Test_isfloat

if __name__ == '__main__':
    unittest.main()
