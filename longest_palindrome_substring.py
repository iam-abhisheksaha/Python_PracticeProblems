from operator import le
import re


def longestPalindrome(s):

    if(len(s) == 1):
        print(s)
    else:
        palindromeLength = 0
        i = 0
        palindrome = []
        while i < len(s):
            palindrome.append(s[i])
            j = i +1
            while j < len(s):
                palindrome.append(s[j])
                print(palindrome)
                if palindrome == palindrome[::-1] and len(palindrome) > palindromeLength:
                    palindromeLength = len(palindrome)
                    print("".join(map(str,palindrome)))
                j += 1
        
            palindrome = []
            i += 1
    






s = "ac"
longestPalindrome(s)

# s = "cbba"
# longestPalindrome(s)