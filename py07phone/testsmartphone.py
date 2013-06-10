#!/usr/bin/env python

"""Unit tests for smartphone.py
"""

import os
import unittest

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
