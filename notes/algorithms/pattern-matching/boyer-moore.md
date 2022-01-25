<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* Constructs a **last table** prior to searching to determine how much to shift the pattern by on a mismatch. 
* Algorithm start comparing from the back of the pattern.  
* Last table maps each character in the alphabet (all characters in pattern and text) to the last index the chracter appears in the pattern. (if the character not in the pattern, use `-1` instead). 

# 2. Operations
1. Constrcut a last table for the pattern. 
2. Align the pattern at the beginning of the text.
3. Compare the last character in the pattern with characer in the text.
4. If match, check for all the previous characters in the pattern. 
5. If not, then take the character in the text, and look up value for that value from last table. 
6. Align the pattern so that index `i` of the pattern is at the mismatching character in the pattern. If the pattern goes to left, then shift pattern right instead by 1.
7. Once match found, shift pattern by right and compares the last character with the text. 

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(m)`|where `m` is the length of the pattern|
|Worst|`O(mn)`|when the last first character in the pattern is always a mismatching character|
|Average| `O(n/m)` `O(n+m)`||

Good for searching large texts. 