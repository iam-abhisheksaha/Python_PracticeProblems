from re import sub
from tkinter import N


def longestSubstring(s):
    substring = []  # Empty string
    maxSubstringLength = 0 # Length of the longest substring
    for i in s:
        if i not in substring:  # Check for not a repating character in list
            substring.append(i) # If not then append to the new list
            length = len(substring) # Length of the new substring
            if length > maxSubstringLength: # CXheck for maximum length of the substring
                maxSubstringLength = length
        elif i in substring: 
            substring = [] # If there is a repeating character initialize the an empty list
            substring.append(i) # If not then append to the new list
    
    print(maxSubstringLength)





s = "abcabcbb"
longestSubstring(s)
s = "aab"
longestSubstring(s)
s = 'dvdf'
longestSubstring(s)