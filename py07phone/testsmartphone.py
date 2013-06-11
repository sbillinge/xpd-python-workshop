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
        return

    def test_sendChat(self):
        """check SmartPhone.sendChat()
        """
        aphone = SmartPhone('A')
        bphone = SmartPhone('B')
        self.assertIsNone(aphone.sendChat(bphone, "hi from A"))
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
        self.assertEqual(2, len(a.getChatHistory(b)))
        self.assertEqual(a.getChatHistory(b), b.getChatHistory(a))
        self.assertEqual(1, len(a.getChatHistory(c)))
        self.assertEqual(a.getChatHistory(c), c.getChatHistory(a))
        return

    def test_printChatHistory(self):
        """check SmartPhone.printChatHistory()
        """
        a, b, c = self.spa, self.spb, self.spc
        with _CaptureStdout() as out:
            a.printChatHistory(b)
        self.assertEqual('', str(out))
        a.sendChat(b, "A to B")
        b.sendChat(a, "B to A")
        with _CaptureStdout() as oa:
            a.printChatHistory(b)
        with _CaptureStdout() as ob:
            b.printChatHistory(a)
        expected = '(A) - A to B\n(B) - B to A\n'
        self.assertEqual(expected, str(oa))
        self.assertEqual(expected, str(ob))
        return

# End of class TestSmartPhone

##############################################################################

class _CaptureStdout(object):

    def __enter__(self):
        import sys
        import cStringIO
        self.save_stdout = sys.stdout
        self.output = cStringIO.StringIO()
        sys.stdout = self.output
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout = self.save_stdout

    def __str__(self):
        return self.output.getvalue()

##############################################################################

if __name__ == '__main__':
    unittest.main()

# End of file
