s = "mom"

def Palindrome(s):
    return s == s[::-1]

s3 = Palindrome(s)
 
if s3:
    print("Valid Palindrome")
else:
    print("Invalid Palindrome")
