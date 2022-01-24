"""
Print the most used word except banned words 
Time Complexity: O(n)

Notes:
Counter() : Used to count
"""
from collections import Counter
import re

# Input
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


##################################################################
words = [
    word
    for word in re.sub("[^\w]", " ", paragraph).lower().split()
    if word not in banned
]

counts = Counter(words)
print(counts.most_common(1)[0][0])
##################################################################
