<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
    - [2.1. Build Failure Table](#21-build-failure-table)
    - [2.2. KMP](#22-kmp)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* KMP(Knuth-Morris-Patt) construct failure table (failure function) to determine how much to shift the pattern by on a mismatch
* KMP initially starts searching from the beginning of the pattern. 
* Failure table is a array of the same length as the pattern, each contains number representing the length of the **longest suffix** (until that point) that is also a prefix in the pattern. (e.g. `rev` in the word `revararev`)

# 2. Operations
## 2.1. Build Failure Table
1. Create two markers `i` and `j`. `i` points to the first character in the pattern, `j` points the second character. First entry of the table is `0`.
2. If `i` and `j` are same, write `i+1` into entry `j` of the table and move **both** `i` and `j` forward by 1. 
3. If different and `i` is **not** at the first character of the pattern, then get the value at index `i-1` and move `i` back to this value. Do not move `j`. 
4. If different and `i` is at the first character of the pattern, then write `0` to `j` and move `j` one forward. Do not move `i`. 
5. Repeat until `j` goes past the end of the string, and all the entries in the table has a value. 
## 2.2. KMP 
1. Align the pattern at the beginning of the text.
2. Compare the first character with the text. 
3. If they match, compare next character and so on. If all matches, then found a match. 
4. If not, AND the mismatch is on the first letter of the pattern, then shift the pattern to the right by 1 and restart comparing. 
5. If not, AND the mismatch is not on the first letter of the pattern, look at `j-1` value in failure table where `j` is the mismatching index. Align the pattern so that `table[j-1]` of the pattern is aligned with mismatching character in the text. Then continute comparing from `table[j-1]` of the pattern. **Do not start from beginning**.
6. Once match found, to search additional match, look at the last index of the failure table. Align the pattern such that the value is aligned **after** the last letter in the text. 

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(m)`|where `m` is the length of the pattern|
|Worst|`O(m+n)`||
|Average| `O(m+n)`||