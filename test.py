#!/usr/bin/env python3
# test file

# import some serious stuff
import os

#test function
def test_exceptions():
    try:
        if not os.path.isdir('/home/pius'):
            raise Exception()
    except:
        print('Jumba Hoi')

test_exceptions()