#!/usr/bin/env python

"""Unit tests for smartphone.py
"""

# version
__id__ = '$Id$'

import os
import unittest

from smartphone import SmartPhone

##############################################################################
class TestSmartPhone(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test___init__(self):
        '''test instantiation of the SmartPhone().
        '''
        smphone = SmartPhone()
        self.assertEqual('', smphone.owner)
        sphjohn = SmartPhone('John')
        self.assertEqual('John', sphjohn.owner)
        return

    def xtest_sendChat(self):
        """check SmartPhone.sendChat()
        """
        aphone = SmartPhone('A')
        bphone = SmartPhone('B')
        self.assertIsNone(sphone.sendChat(bphone, "hi from A"))
        return

    def xtest_receiveChat(self):
        """check SmartPhone.receiveChat()
        """
        return

    def xtest_getChatHistory(self):
        """check SmartPhone.getChatHistory()
        """
        return

    def xtest_printChatHistory(self):
        """check SmartPhone.printChatHistory()
        """
        return

# End of class TestSmartPhone

if __name__ == '__main__':
    unittest.main()

# End of file
