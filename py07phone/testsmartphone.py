#!/usr/bin/env python

"""Unit tests for smartphone.py
"""

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

##############################################################################

class _CaptureStdout(object):

    output = None

    def __enter__(self):
        import sys
        import cStringIO
        self.save_stdout = sys.stdout
        self.output = cStringIO.StringIO()
        sys.stdout = self.output
        return

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.save_stdout

    def __str__(self):
        return '' if self.output is None else self.output.getvalue()

##############################################################################

if __name__ == '__main__':
    unittest.main()

# End of file
