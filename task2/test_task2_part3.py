# -*- coding: utf-8 -*-
"""
COMS W4995
Spring 2018

HW 1
Task 3 Part 1

@author: Daniel Nachajon
UNI: dn2387
"""
#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
import numpy as np
import io

def get_all_unicode_chars_in_file(file_name):
    # Read Input.txt and encode it as a unicode file
    with io.open(file_name, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()
    
    # Having read all the lines, we now loop through and count unicode but we 
    # exclude the newline
    i = 1
    all_unicode_char = []
    for line in all_lines:
        # Remove the newline character
        line = line.rstrip('\n')
        
        # Reset the counter
        unicode_count = 0
        for c in line:
            if ord(c) >= 128:
                unicode_count += 1
                all_unicode_char.append(c)
        if unicode_count > 0:
            print("Line {0}: {1} unicode chars".format(i, unicode_count))
        
        # Increment the line
        i += 1
    
    # Get the the number of distinct chars
    n = len(np.unique(all_unicode_char))
    
    return n, all_unicode_char

def test_task2_part3():
    assert get_all_unicode_chars_in_file('input.txt')[0] == 6