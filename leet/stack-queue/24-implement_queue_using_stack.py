"""
Use stack to support queue operation

Notes:
push(x)
pop() - remove first element
peek() - get first element
empty()
"""

############ Stack Answer O(n) ########
import collections

class MyQueue:
    def __init__(self):
        # 스택 1개로 큐 구현 불가능 
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return len(self.input) == 0 and len(self.output) == 0
########################################
