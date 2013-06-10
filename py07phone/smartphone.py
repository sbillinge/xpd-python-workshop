#!/usr/bin/env

from cellphone import CellPhone
from textmessage import TextMessage

# INSTRUCTIONS:
# 
# (1) Change ONE line below so that SmartPhone has all the functionality
#     of the cell phone.  
#
# (2) Extend the SmartPhone class with a chat feature.

class SmartPhone(object):
    '''SmartPhone is a CellPhone with a chat feature.  It can print
    chat history with all other phones.
    '''

    def sendChat(self, recipient, message):
        '''Send text message to another phone.

        recipient -- instance of another SmartPhone
        message   -- an instance of the TextMessage class being sent

        No Return value.
        Raise ValueError exception if recipient cannot receive chats.
        '''
        # +++your code here+++
        pass


    def receiveChat(self, sender, message):
        '''Accept text message from another phone.

        sender   -- instance of another SmartPhone
        message  -- an instance of the TextMessage class being received

        No Return value.
        '''
        # +++your code here+++
        pass


    def getChatHistory(self, other_phone):
        '''Return chat history with another SmartPhone.

        other_phone  -- instance of another SmartPhone for which the
                        chat history is being looked up

        Return list of TextMessage objects.
        '''
        # +++your code here+++
        pass


    def printChatHistory(self, contactname):
        '''Print chat history with another SmartPhone.

        other_phone  -- instance of another SmartPhone

        No return value.
        '''
        # +++your code here+++
        pass
