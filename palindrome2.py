s = "madam"

def Palindrome(s):
    return s == s[::-1]

s2 = Palindrome(s)
 
if s2:
    print("Valid Palindrome")
else:
    print("Invalid Palindrome")
