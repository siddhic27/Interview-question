s1 ="listen"
s2 ="silent"

def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

check(s1, s2)
