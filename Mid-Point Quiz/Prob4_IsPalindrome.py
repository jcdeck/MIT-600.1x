#Problem 4
#Write a Python function that returns True if aString is a palindrome 
#(reads the same forwards or reversed) and False otherwise. Do not use Python's 
#built-in reverse function or aString[::-1] to reverse strings.

#This function takes in a string and returns a boolean.

def isPalindrome(aString):
    if len(aString) <2: return True
    if aString[0] != aString[-1]:return False
    return isPalindrome(aString[1:-1])