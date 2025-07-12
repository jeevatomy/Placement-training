'''
Given an integer array nums, print "true" if any value appears at least twice in the array, and print "false" if every element is distinct.

Read n, the number of values in the first line, followed by the n numbers in the next line.

Input Format

4 1 2 3 1

Constraints

NA

Output Format

true

'''

from collections import Counter

n=int(input())

arr=list(map(int,input().split()))
dict=Counter(arr)
count=0
for key in dict:
    if dict[key]==2:
        count+=1
if count>0:
    print("true")
else:
    print("false")
