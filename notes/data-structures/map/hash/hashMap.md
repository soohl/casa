# 1. Table of Contents
<!-- TOC -->

- [1. Table of Contents](#1-table-of-contents)
- [2. Maps](#2-maps)
- [3. Hash function](#3-hash-function)
- [4. Collision Strategies](#4-collision-strategies)
    - [4.1. External Chaining (seperate chaining)](#41-external-chaining-seperate-chaining)
    - [4.2. Probing Collision Strategies](#42-probing-collision-strategies)
        - [4.2.1. Linear Probing](#421-linear-probing)
        - [4.2.2. Quadratic Probing](#422-quadratic-probing)
        - [4.2.3. Double Hashing](#423-double-hashing)
- [Efficiencies](#efficiencies)
    - [Close Addressing](#close-addressing)
    - [Open Addressing](#open-addressing)

<!-- /TOC -->

# 2. Maps
Maps have serveral characteristics:

1. Collections of `<key, value>` pairs
2. Searchable
3. Unordered
* Keys are unique (no duplicate keys can exist in one Map) and can not be changed. (key is immutable)
* Maps store and retrieve using the key to identify entries
* Values can change, you can change the value of an entry
* Valus can have duplicates (`<A,3>` and `<B,3>` is OK, `<A,3>` and `<A,4>` is NOT OK)

# 3. Hash function
* It returns an integer value (that hashcode) that represents the key.
* **Why we need it** - the hashcode is used to place the map entry into the backing array and then used to search for an entry when the key is known.
*** How we get it** - every Object has a `.hascode()` method; this method can be customized for any Object you create, but make sure they are relatively unique.
* **How to use it** - compress the hashcode to fit within the bounds of the backing array: `index = hascode % backing array length`.

# 4. Collision Strategies
> What if 2+ entries hash & compress to the same index?

## 4.1. External Chaining (seperate chaining)
* **Closed Addressing** - once we compress the hashcode to find the inex, whis is definitely the index at which the entry with that key will be. 
* Uses a singly linked list at each inde so everyhting that hashes to the same inde will be in a linked list at that index. 

*Example)*

We want to add `{0,1,2,4,11,14,21}` with backing array of `10` indicies.

```
## Hash Map
|index|elements|

[0] - 0
[1] - 1 - 11 - 21
[2] - 2
[3] - null
[4] - 4 - 14
[5] - null
[6] - null
[7] - null
[8] - null
[9] - null
```
We don't want everything to be stored at the same index, so we need to periodically resize when we hit a certain max load factor
* `Load Factor = size / capacity` (the number of entries / backing array capacity)
* Usually the maximum load factor is around 75%
* Make the capacity of the array **prime** to reduce collisions
* Collisions are reduced when resizing to `2N + 1` (odd)

## 4.2. Probing Collision Strategies
* **Open Addressing** - this technique does not ensure that the item you are looking for is in the index. 

### 4.2.1. Linear Probing
If a collisions occurs, we'll just increase the index by one and check again (wrap around back to index 0 if necessary). IOW, we add the number of times we've probed to the original index

*Example)* Put `{8,1,15,5,2,22,50}` in a backing array of length `7`.

| Key | h(k) | Orig index | Probe count | Index: orig index + probe|
|---|---|---|---|---|
|8|1|`8 % 7 = 1`|0|**1 + 0 = 1** *(final)*|
|1|1|`1 % 7 = 1`|0|1 + 0 = 1 *(occupied)*|
| | | |1|**1 + 1 = 2** *(final)* |
15|1|`15 % 7 = 1`|0|1 + 0 = 1 *(occupied)*|
| | | |1|1 + 1 = 2 *(occupied)*|
| | | |2|**1 + 2 = 3** *(final)*|
|5|5|`5 % 7 = 5`|0|**5 + 0 = 5** *(final)*|
|2|2|`2 % 7 = 2`|0|2 + 0 = 2 *(occupied)*|
| | | |1|2 + 1 = 3 *(occupied)*|
| | | |2|**2 + 2 = 4** *(final)*|
|22|1|`22 % 7 = 1`|0|1 + 0 = 1 *(occupied)*|
| | | |1|1 + 1 = 2 *(occupied)*|
| | | |2|1 + 2 = 3 *(occupied)*|
| | | |3|1 + 3 = 4 *(occupied)*|
| | | |4|1 + 4 = 5 *(occupied)*|
| | | |5|**1 + 5 = 6** *(final)*|
|50|1|`50 % 1 = 1`|0 ~ 5| *(occupied)*|
| | | |6|**(1 + 6) % 7 = 0** *(final)*|

`Remove(1)` - origal index : `1 % 7 = 1`
1. `arr[1]` is not null but `8 != 1`, so we keep probing
2. `arr[2]` is not null and `1 == 1`
3. Instead of setting `arr[2] = null`, we'll add a `DEL` marker (because if you make the value null, the next time you search the the value, the searching will stop as it reaches the null value, altough the key may exists later due to probing. So assigning DEL marker indicate to searches further)
4. When we add `15`, we probed passed `1`, so we need some indication to keep probing even after we remove the entry with `1` as the key.

`get(1)`- original index : `1 % 7 = 1`

|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
| |8|DEL|15|DEL| |22|
1. `arr[1]` is not null but `8 != 1`
2. `arr[2]` is deleted, so we keep probing
3. `arr[3]` is not null but `15 != 3`
4. `arr[4]` id deleted, so we keep probing
5. `arr[5]` is null, so `1` is not in the hashMap

### 4.2.2. Quadratic Probing
* Similar to linear probing in that you use the number of probes (0,1,2,3...) to ifnd where you go from the original index. Instead of justr adding the probe number, you add the probe number SQUARED to the original index. *(aims to break up clusters created by linear probing)*

*Example)*Put `{8,1,15,5,2,22,50}` in a backing array of length `7`.

| Key | h(k) | Orig index | Probe count | Index: orig index + probe|
|---|---|---|---|---|
|8|1|`8 % 7 = 1`|0|**1 + 0^2 = 1** *(final)*|
|1|1|`1 % 7 = 1`|0|1 + 0^2 = 1 *(occupied)*|
| | | |1|**1 + 1^2 = 2** *(final)* |
15|1|`15 % 7 = 1`|0|1 + 0^2 = 1 *(occupied)*|
| | | |1|1 + 1^2 = 2 *(occupied)*|
| | | |2|**1 + 2^2 = 5** *(final)*|
|5|5|`5 % 7 = 5`|0|5 + 0^2 = 5 *(occupied)*|
| | | |1|**5 + 1^2 = 6** *(final)*|
|2|2|`2 % 7 = 2`|0|2 + 0^2 = 2 *(occupied)*|
| | | |1|**2 + 1^2 = 3** *(final)*|
|22|1|`22 % 7 = 1`|0|1 + 0 = 1|
| | | |1|1 + 1^2 = 2 *(occupied)*|
| | | |2|1 + 2^2 = 5 *(occupied)*|
| | | |3|**1 + 3^2 = 10** *(final)*|
|50|1|`50 % 1 = 1`|0|1 + 0^2 = 1 *(occupied)*|
| | | |1|1 + 1^2 = 2 *(occupied)*|
| | | |2|1 + 2^2 = 5 *(occupied)*|
| | | |3|1 + 3^2 = 10 *(occupied)*|
| | | |4|**1 + 4^2 = 17** *(final)*|

Stop probing after `N(backing array size)` times, otherwise you may run into infinite loops, when no spaces can be found with this collision strategy (if you cant place the data in N times, resize the HashMap)

### 4.2.3. Double Hashing
More similar to linear probing because you add a factor of the probe count to the original index. The factor is determined by a second hash.

**You have two hash functions:**
1. `h(k) = k % N` (jsut like before)
2. `d(k) = q - k % q` (where `q` is prime and less than the capacity)

*Example)* Put `{8,1,15,5,2,22,50}` in a backing array of length `7`, with `q = 5`.

| Key | h(k) | d(k) | Probe count | Index: `(h(k) + d(k) * p) % N`|
|---|---|---|---|---|
|8|1|`5 - 8 % 5 = 2`|0|**1 + 2(0) = 1 % 7 = 1** *(final)*|
|1|1|`5 - 1 % 5 = 4`|0|1 % 7 = 1 *(occupied)*|
| | | |1|**5 % 7 = 5** *(final)* |
15|1|`5 - 15 % 5 = 5`|0|1 % 7 = 1 *(occupied)*|
| | | |1|**6 % 7 = 6** *(final)*|
|5|5|`5 - 5 % 5 = 5`|0|**5 % 7 = 5** *(final)*|
|2|2|`5 - 2 % 5 = 3`|0|**2 % 7 = 2** *(final)*|
|22|1|`5 - 22 % 5 = 3`|0|1  % 7 = 1 *(occupied)*|
| | | |1|**4 % 7 = 4** *(final)*|
|50|1|`5 - 50 % 5 = 5`|0|1 % 7 = 1 *(occupied)*|
| | | |1|6 % 7 = 6 *(occupied)*|
| | | |2|11 % 7 = 4 *(occupied)*|
| | | |3|16 % 7 = 2 *(occupied)*|
| | | |4|**21 % 7 = 0** *(final)*|

# Efficiencies

## Close Addressing
Insertion, Deletion, Searching would be all `amortized O(n)`. But for inserting (with good hashing function), it would be `O(1)`.

Non-amortized analysis of the time complexity would be `O(n^2)` since we need to resize the backing array.

## Open Addressing
Insertion, Deletion, Searching would be all `amortized O(1)`

Non-amortized analysis of the time complexity would be `O(n^2)` since we need to resize the backing array.