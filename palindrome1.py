s = "radar"

def Palindrome(s):
    return s == s[::-1]

s1 = Palindrome(s)
 
if s1:
    print("Valid Palindrome")
else:
    print("Invalid Palindrome")
