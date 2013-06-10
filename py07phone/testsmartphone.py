#!/usr/bin/env python

"""Unit tests for smartphone.py
"""

import os
import unittest

from cellphone import CellPhone
from smartphone import SmartPhone

##############################################################################
class TestSmartPhone(unittest.TestCase):

    def setUp(self):
        self.spa = SmartPhone('A')
        self.spb = SmartPhone('B')
        self.spc = SmartPhone('C')
        self.dpd = CellPhone('D')
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
        self.assertIsTrue('John', sphjohn.owner)
        return

    def test_sendChat(self):
        """check SmartPhone.sendChat()
        """
        aphone = SmartPhone('A')
        bphone = SmartPhone('B')
        self.assertIsNone(sphone.sendChat(bphone, "hi from A"))
        dphone = CellPhone('D')
        self.assertRaises(ValueError, aphone.sendChat, dphone, "Hi D!")
        return

    def test_receiveChat(self):
        """check SmartPhone.receiveChat()
        """
        from textmessage import TextMessage
        tmsg = TextMessage(self.spa, self.spb, "Hello B!")
        self.assertIsNone(self.spa.receiveChat(tmsg))
        return

    def test_getChatHistory(self):
        """check SmartPhone.getChatHistory()
        """
        a, b, c = self.spa, self.spb, self.spc
        self.assertEqual([], a.getChatHistory(b))
        a.sendChat(b, "A-->B 1")
        b.sendChat(a, "B-->A 1")
        a.sendChat(c, "A-->C 1")
        self.assertEqual(2, a.getChatHistory(b))
        self.assertEqual(a.getChatHistory(b), b.getChatHistory(a))
        self.assertEqual(1, a.getChatHistory(c))
        self.assertEqual(a.getChatHistory(c), c.getChatHistory(a))
        return

    def test_printChatHistory(self):
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
