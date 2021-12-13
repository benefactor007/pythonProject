# coding=utf-8
# Lecture 9: Memory and Search Methods


"""
1) Threshold input size, n zero, smallest problem
>> we can keep dividing, making our problem smaller.
2) How many instances at each division
>> we have a big problem, we divide it into smaller problems
>> How many are we going to divide it into? we divide it into smaller problems until we reach the -
>> -threshold where we can solve it directly
3) [The most important part] combine the sub-solutions






"""


"""
Merge sort
1） the number of copies is order len of the list. 
>> O(len(L))   <- That's linear, and that's sort of at the lower bound
How many comparisons?
>> O(len(L))   <- the order len of the longest list
>> At most, the length of the longer list

Question1: How many times are we going to do a merge?
>> the total complexity of the merge sort?
>> nlog(n)
1) threshold: break it up until I have a list of length 1

triv·i·al | ˈtrivēəl | 琐细地,微不足道地 

"""