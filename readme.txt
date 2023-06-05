These are additional tasks in discrete mathematics
2023, 3rd course BSU

task 1    k-th permutation
Input data format
Given two positive integers n and k, 1≤n≤20,1≤k≤n!.
Output format
Output the k-th permutation of the sequence of numbers 1,2,…,n.

example
3 5 -> 312
3 1 -> 123


task 2    Decryption methods
Alice has a cipher - a string S consisting of numbers, which can be decrypted using the following transformation:
A - 1
B - 2
C - 3
...
Z - 26

She wants to find the number of different ways to decipher S so that the resulting string consists of only uppercase Latin letters. Alice is unfamiliar with combinatorics, so she asks you to help her with the calculation.
Input data format
String S, 1<=|S|<=1e5, 0<=S[i]<=9
Output Format
Print the number of ways to decrypt the original string. Since the answer can be very large, print its remainder modulo 1000000007.

Example standard input standard output13
13  -> 2
113 -> 3
01  -> 0
Note In the first example, "13" can be decoded as "AC" (1, 3) or as "M" (13). In the second example, "113" can be decoded as "AAC" (1, 1, 3), as "KC" (11, 3) or as "AM" (1, 13). In the third example, "01" cannot be decoded so that the resulting string contains only uppercase Latin letters.