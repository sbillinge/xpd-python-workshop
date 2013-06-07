#!/usr/bin/env python

"""Unit tests for the isStringTrue function.
"""

import unittest
from py04exceptunit.isstringtrue import isStringTrue

##############################################################################
class TestIsStringTrue(unittest.TestCase):

    def test_yesno(self):
        "check isStringTrue() for valid arguments."
        self.assertTrue(isStringTrue("yes"))
        self.assertFalse(isStringTrue("no"))
        return

    def test_other(self):
        """check isStringTrue() for a bad argument."""
        self.assertRaises(ValueError, isStringTrue, "dog")
        return

# End of class TestIsStringTrue


if __name__ == '__main__':
    unittest.main()
