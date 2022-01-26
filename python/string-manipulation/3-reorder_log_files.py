"""
Reorder a log files

Time Complexity: O(n)

Notes:
isalpha() = return true if the string only contain alphabet
"""

logs = [
    "dig1 8 1 5 1",
    "let1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero",
]
reordered_logs = [
    "let1 art can",
    "let3 art zero",
    "let2 own kit dig",
    "dig1 8 1 5 1",
    "dig2 3 6",
]

#######################################
letter_log, digit_log = [], []

for log in logs:
    if log.split(" ")[1].isalpha():
        letter_log.append(log)
    else:
        digit_log.append(log)

letter_log.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
print(letter_log + digit_log)
########################################
