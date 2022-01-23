from collections import Counter
import re

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


words = [
    word
    for word in re.sub("[^\w]", " ", paragraph).lower().split()
    if word not in banned
]

print(Counter(words).most_common(1)[0][0])
