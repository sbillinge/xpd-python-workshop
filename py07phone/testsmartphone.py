#!/usr/bin/env python

"""Unit tests for smartphone.py
"""

# version
__id__ = '$Id$'

import os
import unittest

raise NotImplementedError("please update from the MAIN repo later")

# useful variables
thisfile = locals().get('__file__', 'file.py')
tests_dir = os.path.dirname(os.path.abspath(thisfile))
# testdata_dir = os.path.join(tests_dir, 'testdata')

import smartphone

##############################################################################
class TestSmartPhone(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_sendChat(self):
        """check SmartPhone.sendChat()
        """
        return

    def test_receiveChat(self):
        """check SmartPhone.receiveChat()
        """
        return

    def test_getChatHistory(self):
        """check SmartPhone.getChatHistory()
        """
        return

    def test_printChatHistory(self):
        """check SmartPhone.printChatHistory()
        """
        return

# End of class TestSmartPhone

if __name__ == '__main__':
    unittest.main()

# End of file
