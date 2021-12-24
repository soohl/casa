# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

letter_log, digit_log = [], []

for log in logs:
    if log.split(" ")[1].isalpha():
        letter_log.append(log)
    else:
        digit_log.append(log)

letter_log.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))

print(letter_log + digit_log)

# Output: [
#     "let1 art can",
#     "let3 art zero",
#     "let2 own kit dig",
#     "dig1 8 1 5 1",
#     "dig2 3 6",
# ]
