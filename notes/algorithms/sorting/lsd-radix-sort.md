<!-- TOC -->

- [1. Properties](#1-properties)
- [2. Operations](#2-operations)
    - [2.1. Base 10 LSD (least significant digit) Radix Sort](#21-base-10-lsd-least-significant-digit-radix-sort)
- [3. Efficiencies](#3-efficiencies)

<!-- /TOC -->
# 1. Properties
* Stable
* Not Adaptable
* Out-of-place

No Comparisons are actually done. 

# 2. Operations
## 2.1. Base 10 LSD (least significant digit) Radix Sort
1. Create 10 buckets (each bucket as a queue)
2. Take first digit (e.g. `3` in case of `123`) and add the number in to the bucket (e.g. `27` goes in to bucket `7`).
3. Take out number starting from bucket `0`, and put them in array from index 0.
4. Repeat this process for `m` times where `m` is the max digit numbers out of whole elements (e.g. `4` if largest elment is `1000`)
5. To handle negative elements, we need to create seperate `n` number of buckets that only holds negative numbers.

# 3. Efficiencies
|Case|Big O|When|
|---|---|---|
|Best|`O(kn)`|where `k` is the largest digit|
|Worst|`O(kn)`|where `k` is the largest digit|
|Average|`O(kn)`|where `k` is the largest digit|