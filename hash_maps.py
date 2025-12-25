#Counting, frequency, lookups

#Example: first non-repeating character
from collections import Counter

def first_unique_char(s):
    count = Counter(s)

    for i, c in enumerate(s):
        if count[c] == 1:
            return i
        
    return -1

#Complexity: Time O(n), Space O(n)
