<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* Use rolling hash to calculate the has of the pattern and the substring of the text (same length to pattern).
* If hash not matches, it is guaranteed that there the substring mismatches, so shift one to the right.
* If hash matches, substring may matches (cause hash could collide), so check every character one by one. 
* Creating rolling hash is `O(n)` initially, but sliding the hash takes only `O(1)`.
* Initial hash = `sum(text[i] * BASE^(j-i-1))` where `j` is the length of the pattern and `i` increment from `0`.
* Rolling hash = `BASE * (oldHash - text[a] * BASE^(j-1)) + text[b]` where `text[a]` is the character that is being removed from the hash at index `a` and `text[b]` is the character that is being added to the hash. 

# 2. Operations
1. Calculate the hash of the entire pattern and the first `m` characters of the text (`m` is the length of the pattern). 
2. If hash is same, compare each character in the pattern, and if matches than we found matches. 
3. If hash is different, slide hash to the right by one and repeat the process until reach the end of the text. 

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(m)`|where `m` is the length of the pattern|
|Worst|`O(mn)`|pattern hash and the text hash are equal but different in texts|
|Average| `O(m+n)`||