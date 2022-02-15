"""
Input list T and output how long you have to wait before having a warmer day

Notes:
"""

# Input = [73,74,75,71,69,72,76,73]
# Output = [1,1,4,2,1,1,0,0]

############ Stack Answer O(n) ########
T = [73,74,75,71,69,72,76,73]
stack, output = [], [0] * len(T)

for i,t in enumerate(T):
    while stack and t > T[stack[-1]]:
        last = stack.pop()
        output[last] = i - last
    stack.append(i)

print(output)
########################################
