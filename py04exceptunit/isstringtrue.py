
def isStringTrue(s):
    '''Translate string to its logical value.

    Return True or False.
    Raise ValueError if the string is not understood.
    '''
    if s == "yes":
        return True
    elif s == "no":
        return False
    else:
        emsg = 'String must be either "yes" or "no".'
        raise ValueError(emsg)
