<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* Simplest, least efficient string searching algorithm.

# 2. Operations
1. Compare the first character in the text with first character in the pattern.
2. If don't match, shift the pattern to the right by one and compare the first chracter with the current character in the text. 
3. Repeat until find matches or no matches. 
4. If find the matches, check rest of the chracter in the pattern with text.
5. If all matches, found matches.
6. If not, shift one to the right and repeat 3. 

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(m)`|where `m` is the length of the pattern|
|Worst|`O(mn)`|where `n` is the length of the text|
|Average|`O(mn)`||